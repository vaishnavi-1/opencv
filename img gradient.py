import cv2
import numpy as n
from matplotlib import pyplot as plt
img=cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=n.uint8(n.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelCombined=cv2.bitwise_or(sobelX,sobelY)
sobelX=n.uint8(n.absolute(sobelX))
sobelY=n.uint8(n.absolute(sobelY))



titles=['image','laplacian','sobelX','sobelY','sobelCombined']
images=[img,lap,sobelX,sobelY,sobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
