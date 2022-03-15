import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('morp.png', 0)
ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
thresh = 255-thresh
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, cmap='gray')
plt.title('Binary Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(opening, cmap='gray')
plt.title('Operation Opening Result'), plt.xticks([]), plt.yticks([])
plt.show()
