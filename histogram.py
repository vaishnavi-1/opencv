import numpy as n
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread("lena.jpg")
b,g,r=cv.split(img)
cv.imshow("image",img)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)


plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
