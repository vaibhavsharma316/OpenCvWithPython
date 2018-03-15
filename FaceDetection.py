import cv2
import numpy as np
from imutils.video import FPS
import imutils
#Opening Webcam.
#If you have only on webcam in your computer then pass value zero.
#Passing zero will open first connected webcam. If you have more than one
#webcam connected and you want to access second webcam then pass 1.
cam = cv2.VideoCapture(0)
#For increasing the FPS (Optional)
fps = FPS().start()

#For Face Detection
face = cv2.CascadeClassifier("""C:\\Users\\vaibhav\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml""")

def isFace(img):

    # This function will return an array of faces
    faces = face.detectMultiScale(img, 1.2, 1)
    for (x, y, w, h) in faces:
        #Creating rectangle around the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
        #Showing Detected face in live streaming video stream
        cv2.imshow("streaming", img)


    return


while True:

    #Reading frame from webcam. Read function returns an array contains two values
    # return code and image. So i am passing [1] to read image which is at first index.
    # This way is optional you can go with this way too - ret,frame = cam.read()
    frame = cam.read()[1]
    #Reducing the size of frame for faster processing (Optional Step)
    frame = imutils.resize(frame, width=450)

    # This is an optional step to convert color video streaming to gray
    #video streaming to increase the fps
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Calling is Face Function and passing the frame
    isFace(frame)


    key = cv2.waitKey(1) #Will wait for to be pressed for 1 sec

    fps.update() #Optional step

    #If q will be pressed the exit loop
    if key == ord('q'):
        break
    # If c key will be pressed then capture the image from live video stream
    elif key == ord('c'):

        #Writing image to current directory
        cv2.imwrite("captured.jpeg", frame)
        break

#Stop fps thread (Optional step)
fps.stop()
#Release already aquired camera
cam.release()
#Destroy All opened windows
cv2.destroyAllWindows()