import cv2
import os

#讀入照片
image1=cv2.imread('myphoto.jpg')

#顯示像素格式
print(f"height:{image1.shape[0]} pixels")
print(f"width:{image1.shape[1]} pixels")
print(f"channel:{image1.shape[2]} pixels")

#顯示照片
cv2.imshow('img',image1)
cv2.waitKey(0)

from PIL import Image

#讀入照片
image2=Image.open('myphoto.jpg')
type(image2)
Image._show(image2)
print(image2.size)

#縮小照片到指定像素
width=512
height=512
nim=image2.resize((width,height), Image.BILINEAR)
Image._show(nim)
print(nim.size)

#儲存變更照片
nim.save('HW1.jpg')
print(nim.mode,nim.format)
