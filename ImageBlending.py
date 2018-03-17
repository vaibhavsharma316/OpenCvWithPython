import cv2

#Make sure both image must be of same width, height and color

img1 = cv2.imread("nature.jpg")
img2 = cv2.imread("art.jpg")

final_image=cv2.addWeighted(img1,0.4,img2,0.9,0)


cv2.imshow("Image 2",img2)
cv2.imshow("Output",final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()