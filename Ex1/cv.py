import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread("conimage.png")
img2=cv.imread("cvtest.jpg")
px=img[1,1]
#print(img.shape)
#print(img.size)
#print(img.dtype)
plt.show()
print(img2.size)
#b,g,r=cv.split(img2)

  
# Extracting the height and width of an image 
h, w = img2.shape[:2] 
# Displaying the height and width 
#print("Height = {},  Width = {}".format(h, w))
resize = cv.resize(img2, (2000, 2000)) 
plt.imsave("resize.png",resize)
center=(h//2,w//2) 
mat=cv.getRotationMatrix2D(center,200,0.5)
transform=cv.warpAffine(img2,mat,(h,w))
plt.imsave("transform.png",transform)
#cv.imshow("resize",resize)
