from skimage.exposure import rescale_intensity
import numpy as np
import cv2


def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (roi * kernel).sum()
            output[y - pad, x - pad] = k
    output = np.uint8(output)
    return output


image = cv2.imread('noise.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im = gray
num_iter = 15
delta_t = 1/14
kappa = 200
option = 1
br = len(im)
kl = len(im[0, :])
diff_im = np.zeros([br, kl])
diff_im = im
dx = 1
dy = 1
dd = np.sqrt(2)
# 2D convolution masks - finite differences.
hN = np.array(([0, 1, 0], [0, -1, 0], [0, 0, 0]), dtype="int")
hS = np.array(([0, 0, 0], [0, -1, 0], [0, 1, 0]), dtype="int")
hE = np.array(([0, 0, 0], [0, -1, 1], [0, 0, 0]), dtype="int")
hW = np.array(([0, 0, 0], [1, -1, 0], [0, 0, 0]), dtype="int")
hNE = np.array(([0, 0, 1], [0, -1, 0], [0, 0, 0]), dtype="int")
hSE = np.array(([0, 0, 0], [0, -1, 0], [0, 0, 1]), dtype="int")
hSW = np.array(([0, 0, 0], [0, -1, 0], [1, 0, 0]), dtype="int")
hNW = np.array(([1, 0, 0], [0, -1, 0], [0, 0, 0]), dtype="int")
for t in range(num_iter):
    #convoleOutput = convolve(gray, kernel)
    #opencvOutput = cv2.filter2D(gray, -1, kernel)
    nablaN = cv2.filter2D(diff_im, -1, hN)
    nablaS = cv2.filter2D(diff_im, -1, hS)
    nablaW = cv2.filter2D(diff_im, -1, hW)
    nablaE = cv2.filter2D(diff_im, -1, hE)
    nablaNE = cv2.filter2D(diff_im, -1, hNE)
    nablaSE = cv2.filter2D(diff_im, -1, hSE)
    nablaSW = cv2.filter2D(diff_im, -1, hSW)
    nablaNW = cv2.filter2D(diff_im, -1, hNW)
    if (option == 1):
        cN = np.exp(-(nablaN / kappa) ** 2)
        cS = np.exp(-(nablaS / kappa) ** 2)
        cW = np.exp(-(nablaW / kappa) ** 2)
        cE = np.exp(-(nablaE / kappa) ** 2)
        cNE = np.exp(-(nablaNE / kappa) ** 2)
        cSE = np.exp(-(nablaSE / kappa) ** 2)
        cSW = np.exp(-(nablaSW / kappa) ** 2)
        cNW = np.exp(-(nablaNW / kappa) ** 2)
    else:
        cN = 1 / (1 + (nablaN / kappa) ** 2)
        cS = 1 / (1 + (nablaS / kappa) ** 2)
        cW = 1 / (1 + (nablaW / kappa) ** 2)
        cE = 1 / (1 + (nablaE / kappa) ** 2)
        cNE = 1 / (1 + (nablaNE / kappa) ** 2)
        cSE = 1 / (1 + (nablaSE / kappa) ** 2)
        cSW = 1 / (1 + (nablaSW / kappa) ** 2)
        cNW = 1 / (1 + (nablaNW / kappa) ** 2)
    diff_im = diff_im + delta_t * ((1 / (dy ** 2)) * cN * nablaN + (1 / (dy ** 2)) * cS * nablaS + (1 / (dx ** 2)) * cW * nablaW + (1 / (dx ** 2)) * cE * nablaE + (
        1 / (dd ** 2)) * cNE * nablaNE + (1 / (dd ** 2)) * cSE * nablaSE + (1 / (dd ** 2)) * cSW * nablaSW + (1 / (dd ** 2)) * cNW * nablaNW)
cv2.imshow("Original Image", gray)
cv2.imshow("Result Image", np.uint8(diff_im))
cv2.waitKey(0)
cv2.destroyAllWindows()
