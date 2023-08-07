# Basic Pickleball Tracker
During the winter, my family gets together and enjoys playing Pickleball. The inpiration behind this project was to be able to track the ball in a video I took while we were playing. 

![ezgif com-gif-maker (1)](https://github.com/TylerBerzzz/machine-vision-practice/assets/30520534/9fdf1eaa-9462-40c9-9adb-068a3e7fdeed)

## Detection by color
Using openCV & python, one is able to collect frame information from videos they've taken. The method is to convert the frame into HSV (Hue, Saturation, Value), and filter the colors such that only the ball appears. This approach is helpful when the object is a unique color and you have a steady background. Think of a green screen, which is a constant bright green background and enables film makers to do some awesome video effects. 

## Scripts Provided
### BallColorDetector.py
This script identifies the ball using the color values found in HSV_ColorAssist.py

### BoundingBox.py
This script creates a bounding box around the pickleball. It is the main script the code is run from. 

### HSV_ColorAssist.py
This script allows for dynamically adjusting HSV values to find the filtering color values

## Limitations
I chose to show the bounding box if the orange mask was above a certain threshold. This was a quick choice to move on to other projects. 

## Possible improvements
The Hough Transform allows one to identify circles within the frame. This method may allow better identification of the ball when the color is not distinguishable. 
