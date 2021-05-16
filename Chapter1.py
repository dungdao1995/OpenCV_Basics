import cv2

# #IMAGE
# img = cv2.imread('cat.jpg')
#
# cv2.imshow('output', img)
#
# cv2.waitKey(0)


#==========VIDEO ========


# cap  = cv2.VideoCapture('bacphan.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): #Press Q to quit the video
#         break

#========WEBCAM===============

cap = cv2.VideoCapture(0) #0 is the default ID of the webcam

#define the size: height and width: 3,4,10 is the id of the setting
cap.set(3, 640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press Q to quit the video
        break
