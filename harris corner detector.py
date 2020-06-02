import cv2 as cv
import numpy as n
img=cv.imread('chessboard.png')
img=cv.resize(img,(600,600))
cv.imshow('img',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corners=cv.goodFeaturesToTrack(gray,50,0.01,10)
corners=n.int0(corners)
for i in corners:
    x,y=i.ravel()
    cv.circle(img,(x,y),3,255,-1)

cv.imshow("dst",img)

if cv.waitKey(0) & 0xFF==27:
    cv.destroyAllWindows()
