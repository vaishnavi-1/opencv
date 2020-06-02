import numpy as n
import cv2
img1=n.zeros((300,168,3),n.uint8)

img1=cv2.circle(img1,(150,300),50,(255,0,255),5)
img2=cv2.imread('paris.jpg')
bitAnd=cv2.bitwise_and(img2,img1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.imshow("bitand",bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()
