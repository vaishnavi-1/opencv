import cv2
import numpy as n

img=cv2.imread('sudoku task2.jpg')
img=cv2.resize(img,(600,600))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,100,200)
cv2.imshow('edges',edges)
lines=cv2.HoughLinesP(edges,2,n.pi/90,100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()
