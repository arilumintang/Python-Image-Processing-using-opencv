# Syntax for Contrast Stretching
import cv2
import numpy as np
img = cv2.imread('xray.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Real Image', gray)
br = len(img[:, :, 0])
kl = len(img[0, :, 0])
Z = np.zeros([br, kl])
Min = float(np.min(np.min(gray[:, :])))
print("Min=", Min)
Max = float(np.max(np.max(gray[:, :])))
print("Max", Max)
S = Min-Max
for i in range(br):
    for j in range(kl):
        Z[i, j] = (float(gray[i, j])-Min)/S*255
Z = np.uint8(Z)
print("Z", Z)
cv2.imshow('Image of Contrast Stretching', Z)
cv2.waitKey(0)
