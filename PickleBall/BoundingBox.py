# Purpose: Identify the pickle-ball and predict its trajectory
# Developed by: Tyler Bershad
# Acknowledgement: pysource blog
# Last Modified: 8/5/2023

import numpy as np
import cv2
from BallColorDetector import Orange

cap = cv2.VideoCapture('Pickleball.mp4')
output = cv2.VideoWriter("output2.mp4",cv2.VideoWriter_fourcc(*'mp4v'),23.95,(1080 ,1920))

#Load the orange detection
od = Orange()

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    #Get the orange bounding box
    orange_bbox = od.detect(frame)
    x1, y1, x2, y2 = orange_bbox[0]
    mask_sum = orange_bbox[1]

    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)

    #Only show the bounding box if the amount of detected orange reaches a certain threshold
    min_bbox = 233771
    print(mask_sum)
    if mask_sum > min_bbox:
        cv2.circle(frame, (cx, cy), 120, (255, 0, 0), 22)

    resize = cv2.resize(frame, (1080, 1920))
    flip = cv2.flip(resize, -2)

    cv2.imshow("Frame", flip)
    output.write(flip)

    key = cv2.waitKey(50)
    if key == 27:
        break
cv2.destroyAllWindows()
output.release()
cap.release()