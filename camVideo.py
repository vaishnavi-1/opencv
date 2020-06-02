import numpy
import cv2
cap=cv2.VideoCapture('video.mp4')

while(1):
    ret,frame=cap.read()
    cv2.imshow('image',frame)
    if cv2.waitKey(1)==27:
       break

cap.release()
cv2.destroyAllWindows
               
