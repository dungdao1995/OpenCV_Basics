#SHAPE AND TEXT on imgae

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape[1])

#img[:] = 255,0,0

#add the line
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0),3) #start-end position, color, thickness

#Retangle

cv2.rectangle(img, (0,0), (250, 350), (0,0,255), 2) #like the bounding box
#Circle
cv2.circle(img, (400,50), 30 , (255,255,0), 5)

#Text

cv2.putText(img, 'OpenCV DKD', (300,150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150,0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)