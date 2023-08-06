# Purpose: Identify the pickle-ball and predict its trajectory
# Developed by: Tyler Bershad
# Acknowledgement: pysource blog
# Last Modified: 8/5/2023

import numpy as np
import cv2
class Orange:
    def __init__(self):
        # Create mask for orange color
        self.low_orange = np.array([0, 149, 66])
        self.high_orange = np.array([23, 255, 255])

    def detect(self, frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks with color ranges
        mask = cv2.inRange(hsv_frame, self.low_orange, self.high_orange)
        orange = cv2.bitwise_and(frame, frame, mask=mask)

        # Find Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        #Calculate the total pixel sum of the orange mask. This will help with drawing a good bounding box
        mask_sum = int(orange.sum())

        #print(total_sum) #Debug

        box = (0, 0, 0, 0)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            box = (x, y, x + w, y + h)
            break

        return box, mask_sum