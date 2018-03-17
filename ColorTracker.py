import cv2
import numpy as np

#Opening Webcamera
cam = cv2.VideoCapture(0)
#Green color minimum value
lower_bound=np.array([60,100,100])
#Green color maximum value
upper_bound=np.array([70,255,255])

while True:
    #Reading frames
    frame = cam.read()[1]
    #waiting for the to be pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        #If q key pressed then break the loop
        break

    else:
        #Converting frame to HSV Color space
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #Creating a black Mask
        mask = cv2.inRange(hsv,lower_bound,upper_bound)
        #Extracting only required color from image and setting mask on rest of the image
        result = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("frame",frame)
        cv2.imshow("mask",mask)
        #Showing Extracted
        cv2.imshow("result", result)
cam.release()
cv2.destroyAllWindows()