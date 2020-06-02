import numpy as n
import cv2 as cv
img=cv.imread('apples.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv.split(img)
img=cv.merge((b,g,r))



cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
