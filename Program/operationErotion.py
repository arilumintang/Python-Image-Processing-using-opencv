import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('morp.png', 0)
ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
erosi = cv2.erode(thresh, kernel, iterations=1)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, cmap='gray')
plt.title('Binary Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(erosi, cmap='gray')
plt.title('Erotion Result'), plt.xticks([]), plt.yticks([])
plt.show()
