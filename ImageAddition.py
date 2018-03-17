
#Make sure both image must be of same height width and color


import cv2
img1 = cv2.imread("nature.jpg")

img2 = cv2.imread("art.jpg")

#numpy addition
img3=img1 + img2
cv2.imshow("addition",img3)

#opencv addition using open cv function
cv2.imshow("opencv addition",cv2.add(img1,img2))

cv2.waitKey(0)
cv2.destroyAllWindows()