import cv2


img = cv2.imread("nature.jpg")

cv2.putText(img,"Vaibhav Sharma",(250,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

cv2.imshow("Text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
