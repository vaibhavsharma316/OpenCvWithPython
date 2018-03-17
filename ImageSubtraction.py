
#Make sure both image must be of same height width and color


import cv2
img1 = cv2.imread("nature.jpg")

img2 = cv2.imread("art.jpg")

#numpy subtraction
img3=img1 - img2
cv2.imshow("subtraction",img3)

#opencv subtraction using open cv function
cv2.imshow("opencv subtraction",cv2.subtract(img1,img2))

cv2.waitKey(0)
cv2.destroyAllWindows()