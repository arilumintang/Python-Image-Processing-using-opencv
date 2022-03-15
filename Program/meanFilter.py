import numpy as np
import cv2
img = cv2.imread('Xraynoisy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', gray)
br = len(img[:, :, 0])
kl = len(img[0, :, 0])
ZZ = np.zeros([br, kl])
H = 1/25*np.ones([br, kl])
print(H)
for i in range(br-5):  # =2:br-3
    I = i+2
    for j in range(kl-5):  # j=2:kl-3
        J = i+1
        LL = 0
        for k in range(5):  # k=-2:2
            K = 2-k
            for l in range(5):  # l=-2:2
                L = 2-l
                LL = LL+H[3+K, 3+L]*gray[i+K, j+L]
        ZZ[i, j] = LL
print("ZZ", ZZ)
ZZ = np.uint8(ZZ)
print(ZZ)
cv2.imshow('Image of Mean Filter', ZZ)
cv2.waitKey(0)
