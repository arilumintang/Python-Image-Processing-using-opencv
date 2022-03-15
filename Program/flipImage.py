# Syntax for flip the image
import cv2
img = cv2.imread("example.jpeg")
# Syntax for flip the image vertically
flipVertical = cv2.flip(img, 0)
cv2.imshow("Real", img)
cv2.imshow("Flip Vertikal", flipVertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
