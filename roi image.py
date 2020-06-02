import numpy as n
import cv2 
img=cv2.imread("apples.jpg")
print(img)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

paris=img[197:251,46:132]
img[20:50,44:122]=paris

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
