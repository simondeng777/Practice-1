import cv2
import os

image1=cv2.imread('lena30.jpg')
print(f"height:{image1.shape[0]} pixels")
print(f"width:{image1.shape[1]} pixels")
print(f"channel:{image1.shape[2]} pixels")
cv2.imshow('img',image1)
cv2.waitKey(0)

image2=cv2.imread('lena30.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',image2)
print(image2.shape)
cv2.imwrite('lenagray.jpg',image2)
cv2.waitKey(0)

#介紹PLT套件
from matplotlib import pyplot as plt
plt.imshow(image1)
plt.show()
plt.waitforbuttonpress

img_rgb=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()
plt.waitforbuttonpress

plt.imshow(image2)
plt.show()
plt.waitforbuttonpress

plt.imshow(image2,cmap='gray')
plt.imsave('lenagray-plt.jpg',image2)
plt.show()
plt.waitforbuttonpress

#介紹IMAGE套件
from PIL import Image
image3=Image.open('lena_gray.gif')
type(image3)
Image._show(image3)
print(image3.size)

width=200
ratio=float(width)/image3.size[0]
height=int(image3.size[1]*ratio)
nim=image3.resize((width,height), Image.BILINEAR)
print(nim.size)
Image._show(nim)

nim=nim.convert('RGB')
nim.save('lena_resize.jpg')
print(nim.mode,nim.format)

image4=Image.open('lena_color.gif')
print(type(image4))
print(image4.mode,image4.format)

image4=image4.convert('RGB')
image4.save('lena_color.jpg')
print(image4.mode,image4.format)

image5=Image.open('lena_color.jpg')
print(image5.mode,image5.format)

imgR=nim.transpose(Image.ROTATE_180)
Image._show(imgR)

imgF=nim.transpose(Image.FLIP_LEFT_RIGHT)
Image._show(imgF)
