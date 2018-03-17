
#Make sure both image must be of same height width and color


import cv2
img1 = cv2.imread("nature.jpg")

img2 = cv2.imread("art.jpg")

#numpy Division
img3=img1 * img2

cv2.imshow("Division",img3)

#opencv Division using open cv function
cv2.imshow("opencv Division",cv2.divide(img1,img2))

cv2.waitKey(0)
cv2.destroyAllWindows()