import cv2
import numpy as np
import flevelset as lv
import time
import matplotlib.pyplot as plt
img = cv2.imread('data1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ln, cl = len(gray), len(gray[0])
tms = 0.2
it_in = 10
it_out = 80
sig = 1.5
img_s = cv2.GaussianBlur(gray, (15, 15), sig)


def grad(x):
    return np.array(np.gradient(x))


def norm(x, axis=0):
    return np.sqrt(np.sum(np.square(x), axis=axis))


def stopping_fun(x):
    return 1. / (1. + norm(grad(x))**2)


g = stopping_fun(img_s)
c0 = 2
phi = c0*np.ones((ln, cl))
phi[5:-5, 5:-5] = -c0
def tresh0(x): return 255 if x <= 2 else 0


tresh = np.vectorize(tresh0)
for i in range(it_out):
    phi = lv.levelset(phi, g, tms, it_in)
    gbr = tresh(phi)
    cv2.imshow('Iteration', np.uint8(gbr))
    cv2.waitKey(1)
    time.sleep(0.1)
cv2.destroyAllWindows()
# read the image
image = np.uint8(gbr)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)
print(pixel_values.shape)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 2
_, labels, (centers) = cv2.kmeans(pixel_values, k, None,
                                  criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
labels = labels.flatten()
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)
plt.imshow(segmented_image)
plt.show()
