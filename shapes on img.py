import numpy as n
import cv2
img=n.zeros([512,512,3],n.uint8)
img=cv2.line(img,(0,0),(206,206),(255,0,255),4)
img=cv2.circle(img,(206,200),80,(255,0,0),6)
img=cv2.rectangle(img,(100,0),(300,300),(0,255,0),3)
img=cv2.arrowedLine(img,(206,206),(500,500),(147,96,41),6)
img=cv2.ellipse(img,(300,300),(60,30),0,0,360,(0,0,255),5)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'vaishu',(20,100),font,5,(255,255,0),10,cv2.LINE_AA)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,255,0),1)
        points.append((x,y))
        if len(points)>=2:
               cv2.line(img,points[-1],points[-2],(0,0,255),7)
        cv2.imshow('image',img)
               

cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
