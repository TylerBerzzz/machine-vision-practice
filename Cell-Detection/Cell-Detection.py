# Purpose: Identify the cells and the wells in the source image
# Developed by: Tyler Bershad
# Last Modified: 8/7/2023

#Approach:
#Count the rings - Use Hough Transform
#Count the blue and green - use inRange and Blob Detection

import numpy as np
import cv2

frame = cv2.imread("SampleImage.jpg", cv2.IMREAD_COLOR)

# convert the image to grayscale format
img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(img_gray, 5)
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

while True:
    #Separate Blue Color Cells:
    low_blue = np.array([106, 104, 0])
    high_blue = np.array([255, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #Separate Green Color Cells:
    low_green = np.array([0, 90, 0])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    #Blob Detection:
    # Initialize parameters for blob detection
    params = cv2.SimpleBlobDetector_Params()
    params.filterByInertia = True
    params.filterByArea = True
    params.filterByCircularity = True
    params.filterByConvexity = True
    params.filterByColor = False

    params.minArea = 2
    params.maxArea = 600
    params.minCircularity = 0
    params.maxCircularity = 1
    params.minConvexity = 0
    params.minInertiaRatio = 0
    params.maxInertiaRatio = 1

    #Green Blob Detect --------------------------------------------
    detector_g = cv2.SimpleBlobDetector_create(params)
    keypoints_g = detector_g.detect(green)

    blank = np.zeros((1, 1))
    blobs_g = cv2.drawKeypoints(green, keypoints_g, blank, (0, 0, 255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    text = "Green Stained Cell Count: " + str(len(keypoints_g))
    cv2.putText(blobs_g, text, (350, 515),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Blue Blob Detect --------------------------------------------
    detector_b = cv2.SimpleBlobDetector_create(params)
    keypoints_b = detector_g.detect(blue)

    blank = np.zeros((1, 1))
    blobs_b = cv2.drawKeypoints(blue, keypoints_b, blank, (0, 0, 255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    text = "Blue Stained Cell Count: " + str(len(keypoints_b))
    cv2.putText(blobs_b, text, (350, 515),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


    #Outer Circle Detection
    rows = gray.shape[0] #returns a tuple with each index having the number of corresponding elements.
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,  rows/100, param1=100, param2=30, minRadius=10, maxRadius=25)
    newFrame = frame.copy()

    if circles is not None: #If the found circles are not empty
        circles = np.uint16(np.around(circles)) #Round an array to the given number of decimals.
        for i in circles[0, :]:
            center = (i[0], i[1])
            # Draw the circle center
            cv2.circle(newFrame, center, 1, (0, 100, 100), 2)
            # Draw the circle outline
            radius = i[2]
            cv2.circle(newFrame, center, radius, (255, 0, 255), 2)
            count_txt = "Outer Cell Count = "+str(len(circles[0]))
            cv2.putText(newFrame,text= count_txt, org = (400,515),color = (255,255,255), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, thickness=2)

    # Show the regular and filtered images
    # cv2.imshow("regular", frame)
    # cv2.imshow("Green Cells", green)
    # cv2.imshow("Blue Cells", blue)

    # Show the identified circles
    cv2.imshow("detected circles", newFrame)
    cv2.imshow("Identified Green Blobs", blobs_g)
    cv2.imshow("Identified Blue Blobs", blobs_b)

    # Press 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord('q'):
        cv2.imwrite("detectedWells.jpg", newFrame)
        cv2.imwrite("detectedGreen.jpg", blobs_g)
        cv2.imwrite("detectedBlue.jpg", blobs_b)
        cv2.destroyAllWindows()
        break

