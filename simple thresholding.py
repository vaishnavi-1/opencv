import numpy as n
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('lena.jpg',-1)

cv.imshow('image',img)
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
