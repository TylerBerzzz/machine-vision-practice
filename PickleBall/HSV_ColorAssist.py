# Purpose: Identify the pickle-ball and predict its trajectory
# Developed by: Tyler Bershad
# Acknowledgement: pysource blog
# Last Modified: 8/5/2023

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture('Pickleball.mp4')

#Create Trackbars that will assist with choosing the right color range
cv2.namedWindow("Trackbars")
cv2.createTrackbar("low - H","Trackbars", 0, 255, nothing)
cv2.createTrackbar("low - S","Trackbars", 149, 255, nothing)
cv2.createTrackbar("low - V","Trackbars", 66, 255, nothing)
cv2.createTrackbar("high - H","Trackbars", 23, 255, nothing)
cv2.createTrackbar("high - S","Trackbars", 255, 255, nothing)
cv2.createTrackbar("high - V","Trackbars", 255, 255, nothing)

while(cap.isOpened()):
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Make the Trackbar dynamic
    l_h = cv2.getTrackbarPos("low - H", "Trackbars")
    l_s = cv2.getTrackbarPos("low - S", "Trackbars")
    l_v = cv2.getTrackbarPos("low - V", "Trackbars")
    u_h = cv2.getTrackbarPos("high - H", "Trackbars")
    u_s = cv2.getTrackbarPos("high - S", "Trackbars")
    u_v = cv2.getTrackbarPos("high - V", "Trackbars")

    #I want orange:
    low_orange = np.array([l_h, l_s, l_v])
    high_orange = np.array([u_h, u_s, u_v])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)

    #Flip the video and resize it
    resize1 = cv2.resize(frame, (700, 1200))
    flip1 = cv2.flip(resize1,0)
    resize2 = cv2.resize(orange, (700, 1200))
    flip2 = cv2.flip(resize2, 0)

    cv2.imshow("regular", flip1)
    cv2.imshow("ballDetect", flip2)


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()