import cv2

img=cv2.inread('village.png')

#now detect canny edge

canny=cv2.Canny(img, 200, 255)

cv2.imshow("original",img)
cv2.inshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
