import cv2

#Reading Image
img = cv2.imread("nature.jpg")

#Showing Original Image (BGR ColorSpace)
cv2.imshow("Original",img)

#Converting Image To GrayScale ColorSpace
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray",gray)

#Converting Image To HSV ColorSpace
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("HSV",hsv)

#Converting Image To LUV ColorSpace
luv = cv2.cvtColor(img,cv2.COLOR_BGR2LUV)

cv2.imshow("LUV",luv)


cv2.waitKey(0)
cv2.destroyAllWindows()