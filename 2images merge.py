
import numpy as n
import cv2
img=cv2.imread('apples.jpg')
cv2.imshow('ori image',img)
img2=cv2.imread('paris.jpg')
cv2.imshow('ori img2',img2)
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
img=cv2.resize(img,(512,512))
img2=cv2.resize(img,(512,512))
dst=cv2.addWeighted(img,0.5,img2,2.5,0)


cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
