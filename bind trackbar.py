import numpy as n
import cv2 as cv
def nothing(x):
    pass

while(True):
    frame=cv.imread('smarties.png')
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_b=n.array([52,43,227])
    u_b=n.array([255,255,255])

    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    k=cv.waitKey(1) & 0xFF
    if k==27:
        break

    
cv.destroyAllWindows()
