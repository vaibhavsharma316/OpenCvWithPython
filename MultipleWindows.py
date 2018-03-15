import cv2


gray_img=cv2.imread("nature.jpg",cv2.IMREAD_GRAYSCALE)
color_img=cv2.imread("nature.jpg",cv2.IMREAD_COLOR)
cv2.imshow("gray",color_img)
cv2.imshow("color",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()