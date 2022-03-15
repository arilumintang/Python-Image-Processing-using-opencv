import cv2
import numpy as np
img = cv2.imread('xray.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
ddepth = cv2.CV_16S
kernel_size = 3
img_laplacian = cv2.Laplacian(img_gaussian, ddepth, ksize=kernel_size)
cv2.imshow("Original Image", img)
cv2.imshow("Laplacian", np.uint8(img_laplacian))
cv2.waitKey(0)
cv2.destroyAllWindows()
