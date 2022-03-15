import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('xray.jpeg')
Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Bin = np.zeros(256)
for i in range(256):
    Bin[i] = i
plt.figure(1)
n, bins, patches = plt.hist(Gray.ravel(), bins=Bin, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram for Component Gray Scale Before Histogram Equalization')
cv2.imshow('Original Image', Gray)
equalGray = cv2.equalizeHist(Gray)
plt.figure(2)
n, bins, patches = plt.hist(equalGray.ravel(), bins=Bin,
                            color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram for Component Gray Scale After Histogram Equalization')
cv2.imshow('Equalization Result', equalGray)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
