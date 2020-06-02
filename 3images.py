import numpy
import cv2
img=cv2.imread('3-8.jpg')
img1=cv2.imread('paris.jpg')
img2=cv2.imread('Tyrannosaurus-Rex-Struthiomimus-dinosaurs.jpg')

cv2.imshow('image',img)
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows
               
