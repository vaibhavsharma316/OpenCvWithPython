import numpy as np
import cv2

#Creating Black image of 512x512 pixels
img = np.zeros((512,512,3),np.uint8)

#Creating Rectangle
cv2.rectangle(img,(100,50),(200,100),(255,0,0),3)

cv2.imshow("Rectangle",img)

cv2.waitKey(0)
cv2.destroyAllWindows()