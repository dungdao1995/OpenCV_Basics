import cv2
import numpy as np

img = cv2.imread('cat.jpg')

kernel = np.ones((5,5), np.uint8)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray,(7,7), 0)

#Find the edge of image
imgCanny = cv2.Canny(img, 150,200)

#Thickness of image of edge
imgDilation = cv2.dilate(imgCanny , kernel, iterations=2) #iteration: how much

#make it thinner
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)



# cv2.imshow('Gray Image', imgGray)
#
# cv2.imshow('Blur Image', imgBlur)

cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilation Image', imgDilation)
cv2.imshow('Eroded Image', imgEroded)

cv2.waitKey(0)