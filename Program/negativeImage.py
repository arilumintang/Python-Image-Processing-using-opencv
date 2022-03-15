# Syntax for negative image with opencv-python (cv2)
import numpy as np
import cv2
img = cv2.imread("example.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
br = len(gray)
kl = len(gray[0])
negativeImage = np.uint8(np.zeros([br, kl]))
for i in range(br):
    for j in range(kl):
        negativeImage[i, j] = 255-gray[i, j]
cv2.imshow("Real Image", img)
cv2.imshow("Negative Image", negativeImage)
cv2.waitKey(0)
cv2.destroyAllWindows()