# Basic Pickleball Tracker
During the winter, my family gets together and enjoys playing Pickleball. The inpiration behind this project was to be able to track the ball in a video I took while we were playing. 



## Detection by color
Using openCV & python, one is able to collect frame information from videos they've taken. The method is to convert the frame into HSV (Hue, Saturation, Value), and filter the colors such that only the ball appears. This approach is helpful when the object is a unique color and you have a steady background. Think of a green screen, which is a constant bright green background and enables film makers to do some awesome video effects. 

## Limitations
I chose to show the bounding box if the orange mask was above a certain threshold. This was a quick choice to move on to other projects. 

## Possible improvements
The Hough Transform allows one to identify circles within the frame. This method may allow better identification of the ball when the color is not distinguishable. 
