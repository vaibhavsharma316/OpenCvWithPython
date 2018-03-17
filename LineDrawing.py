import numpy as np
import cv2

#Creating Black image of 512x512 pixels
img = np.zeros((512,512,3),np.uint8)

#Creating Line
cv2.line(img,(511,0),(0,511),(255,0,0),5)

cv2.imshow("Line",img)

cv2.waitKey(0)
cv2.destroyAllWindows()