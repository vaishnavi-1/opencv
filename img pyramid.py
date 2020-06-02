import cv2
import numpy as n
img=cv2.imread('lena.jpg')
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
layer=gp[5]
cv2.imshow('upper level gauss pyr',layer)
lp=[layer]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)
    print(i)   
    
cv2.imshow("orig img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
