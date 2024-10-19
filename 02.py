#叫cv2套件
import cv2

#讀照片進程式並觀看
image1=cv2.imread('lena30.jpg')
cv2.imshow('img',image1)
cv2.waitKey(0)

#將照片放大或縮小
image2=cv2.resize(image1, (0,0), fx=0.5, fy=0.5)
cv2.imshow('img',image2)
cv2.waitKey(0)

#讀影片進程式並抓第一張照片
cap=cv2.VideoCapture('60秒台灣.mp4')

ret, frame = cap.read()
if ret:
     cv2.imshow('video1', frame) 
cv2.waitKey(0)

#讀取攝像頭並抓第一張照片
cap=cv2.VideoCapture(0)

ret, frame = cap.read()
if ret:
     cv2.imshow('video1', frame) 
cv2.waitKey(0)

#讀影片進程式並播放
cap=cv2.VideoCapture('60秒台灣.mp4')
while True:
     ret, frame = cap.read()
     if ret:
          cv2.imshow('video1', frame)
     else:
          break
     cv2.waitKey(1)