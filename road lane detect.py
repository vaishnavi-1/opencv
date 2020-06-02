import matplotlib.pylab as plt
import cv2
import numpy as n
def region_of_interest(img,vertices):
    mask=n.zeros_like(img)
    match_mask_color=(255)
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image
def draw_the_lines(img,lines):
    img=n.copy(img)
    blank_image=n.zeros((img.shape[0],img.shape[1],3),dtype=n.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(255,0,255),3)
            
    img=cv2.addWeighted(img,0.8,blank_image,1,0.0)
    return img

image=cv2.imread('road.jfif')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(image.shape)
height=image.shape[0]
width=image.shape[1]
region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)]
gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
canny_image=cv2.Canny(gray_image,100,200)
cropped_image=region_of_interest(canny_image,n.array([region_of_interest_vertices],n.int32))
lines=cv2.HoughLinesP(cropped_image,rho=6,theta=n.pi/60,threshold=160,lines=n.array([]),minLineLength=40,maxLineGap=25)
image_with_line=draw_the_lines(image,lines)
plt.imshow(canny_image)

plt.show()
