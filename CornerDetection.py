import cv2
import numpy as np

# read in image
img = cv2.imread('opencv-corner-detection-sample.jpg')
# convert img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# converting pixel values to float32 equivalent
gray = np.float32(gray)

# param1 is image, param2 is number to find, param3 is quality,
#  param4 is min distance between corners
# always convert to float because this function only accepts floats
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# Convert to basic int value used on system
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    # image, center, radius, color, fill
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('Corner', img)
cv2.waitKey()




