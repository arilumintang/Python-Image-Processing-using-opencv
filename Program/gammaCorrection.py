# Syntax for Correction Gamma
import cv2
import numpy as np
img = cv2.imread('bacteria2.jpeg')
cv2.imshow('Real Image', img)
br = len(img[:, :, 0])
kl = len(img[0, :, 0])
Z = np.zeros([br, kl, 3])
c = 1
n = 1.1
for i in range(br):
    for j in range(kl):
        for k in range(3):
            Z[i, j, k] = c*np.float(img[i, j, k])**n
            if(Z[i, j, k] >= 255):
                Z[i, j, k] = 255
Z = np.uint8(Z)
cv2.imshow('Image of Correction Gamma', Z)
cv2.waitKey(0)
