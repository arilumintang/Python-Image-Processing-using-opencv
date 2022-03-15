import cv2
import numpy as np
img = cv2.imread('tomatoLeaves.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ln = len(gray)
cl = len(gray[0, :])
Y = np.zeros([ln, cl])
for i in range(ln):
    for j in range(cl):
        if gray[i, j] < 128:
            Y[i, j] = 0
        else:
            Y[i, j] = 255
Y = np.uint8(Y)
cv2.imshow('Gray Image', img)
cv2.imshow('Binary Image', Y)
cv2.waitKey(0)
cv2.destroyAllWindows()
