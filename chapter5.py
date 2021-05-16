#WARP PRESPECTIVE

import cv2
import numpy as np

img = cv2.imread('cards.jpg')

width, height = 250, 350

pts1 = np.float32([[111,219],[287,188],[154,482], [352,440]]) # 4 points = 4 corners on the pic

pts2 = np.float32([[0,0],[width,0],[0,height], [width,height]]) # the new pic with the size

matrix = cv2.getPerspectiveTransform(pts1,pts2) #From the matrix of 4 location of corner =>> new pic

imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow('img', img)
cv2.imshow('imgOutput', imgOutput)


cv2.waitKey(0)