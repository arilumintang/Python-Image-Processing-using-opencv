# Syntax for open and show the image
import cv2
img = cv2.imread("example.jpeg")
cv2.imshow("Real", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
