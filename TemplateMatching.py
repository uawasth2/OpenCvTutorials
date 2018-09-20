import cv2
import numpy as np

img_bgr = cv2.imread('PCSetup.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# imports as gray
template = cv2.imread('PortOnPC.jpg', 0)
# a method of getting the width and height of our image
w, h = template.shape[::-1]

# takes image, template to match, and a method to match
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# A threshold to see how much each point matches with our threshold in our image
threshold = 0.8
# gets the array of all locations as x,y coords that fit our threshold in our image
loc = np.where(res >= threshold)

# gets every point in our array of locations
for pt in zip(*loc[::-1]):
    # Then draws rectangle with pt and then the w,h of our template image to match the size in the actualy image
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)