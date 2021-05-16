# RESIZE THE IMAGE AND CROPPING

import cv2
import numpy as np

img = cv2.imread('car.jpg')

kernel = np.ones((5,5), np.uint8)


print(img.shape) # Height, width, RGB: H = rows in matrix, W = columns in matrix

imgResize = cv2.resize(img, (225,150)) #define W and H : in the openCV Width and Height, in the matrix: H and W
print(imgResize.shape)


imgCropped = img[0:200, 100:300]

cv2.imshow('Image', img)
cv2.imshow('ImageResize', imgResize)
cv2.imshow('imgCropped', imgCropped)
cv2.waitKey(0)