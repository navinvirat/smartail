import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import cv2 as cv
d=pd.read_csv("mnist_train.csv")
l=d['label']
data=d.drop("label",axis=1)
plt.figure(figsize=(7,7))
i=0 
j=1
mdata1=data.iloc[i].to_numpy().reshape(28,28)
mdata2=data.iloc[j].to_numpy().reshape(28,28)
plt.imsave("mnist.png",mdata1,cmap="gray")
plt.imsave("mnist2.png",mdata2,cmap="gray")
con_image=np.concatenate((mdata1,mdata2),axis=-1)
plt.imsave("con2.png",con_image,cmap="gray")
img=cv.imread("con2.png")
print(img.size)
print(l[i])
print(l[j])



