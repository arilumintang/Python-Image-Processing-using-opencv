import numpy as np
import cv2
import matplotlib.pyplot as plt


def hist(R):
    line = len(R)
    clmn = len(R[0, :])
    H = np.zeros(256)
    for i in range(line):
        for j in range(clmn):
            for k in range(256):
                if (R[i][j] == k):
                    H[k] = H[k] + 1
    n = line * clmn
    for k in range(256):
        H[k] = H[k] / n
    return H


img = cv2.imread('leafData.jpeg')
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
R = RGB[:, :, 2]
G = RGB[:, :, 1]
B = RGB[:, :, 0]
Bin = np.zeros(256)
for i in range(256):
    Bin[i] = i
HistR = hist(R)
HistG = hist(G)
HistB = hist(B)
plt.plot(Bin, HistR, '-r')
plt.plot(Bin, HistG, '-g')
plt.plot(Bin, HistB, '-b')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram for the Image')
plt.legend(["Component R", "Component G", "Component B"])
plt.show()
cv2.imshow("Color Image", RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
