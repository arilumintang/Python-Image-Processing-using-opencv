import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('morp.png', 0)
ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, cmap='gray')
plt.title('Binary Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(closing, cmap='gray')
plt.title('Operation Closing Result'), plt.xticks([]), plt.yticks([])
plt.show()
