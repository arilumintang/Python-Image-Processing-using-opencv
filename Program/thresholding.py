import cv2
img = cv2.imread('tomatoLeaves.jpg', 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Gray Image', img)
cv2.imshow('Binary Image', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
