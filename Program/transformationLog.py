# Syntax for Transformation Log
import cv2
import numpy as np
img = cv2.imread('bacteria2.jpeg')
cv2.imshow('Real Image', img)
br = len(img[:, :, 0])
kl = len(img[0, :, 0])
Z = np.zeros([br, kl, 3])
c = 30
for i in range(br):
    for j in range(kl):
        for k in range(3):
            Z[i, j, k] = c*np.log(1+float(img[i, j, k]))
Z = np.uint8(Z)
cv2.imshow('Image of Transformation Log', Z)
cv2.waitKey(0)
