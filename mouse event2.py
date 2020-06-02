import numpy as n
import cv2 as cv

def click_event(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+','+str(y)
        cv.putText(img,strXY,(x,y),font,0.5,(255,0,255),2)
        cv.imshow('image',img)
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        red=img[y, x, 1]
        green=img[y,x,2]
        font=cv.FONT_HERSHEY_PLAIN
        strBGR=str(blue)+','+str(green)+','+str(red)
        cv.putText(img,strBGR,(x,y),font,1,(0,255,0),2)
        cv.imshow('image',img)
img=cv.imread('paris.jpg')
cv.imshow('image',img)
cv.setMouseCallback('image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()
