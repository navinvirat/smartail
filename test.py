import numpy as np
import matplotlib.pyplot as plt
one=[[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,1,1,1,0]]
two=[[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0],[0,1,0,0,0],[0,1,1,1,0]]
three=[[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0]]
four=[[0,1,0,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,1,0]]
five=[[0,1,1,1,0],[0,1,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0]]
six=[[0,1,1,1,0],[0,1,0,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0]]
seven=[[0,1,1,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0]]
eight=[[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0]]
nine=[[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0]]
zero=[[0,1,1,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,1,1,0]]
plt.imshow(one)
plt.imshow(two)
plt.imsave("1.png",one)
plt.imsave("2.png",two)
plt.imsave("3.png",three)
plt.imsave("4.png",four)
plt.imsave("5.png",five)
plt.imsave("6.png",six)
plt.imsave("7.png",seven)
plt.imsave("8.png",eight)
plt.imsave("9.png",nine)
plt.imsave("0.png",zero)
conc_img = np.concatenate((one,two,three,four,five,six,seven,eight,nine,zero), axis=-1)
conc_img2 = np.concatenate((one,two,three,four,five,six,seven,eight,nine,zero), axis=-2)
plt.imsave("conimage.png",conc_img,cmap="gray")
plt.imsave("conimage2.png",conc_img2,cmap="gray")
plt.show()