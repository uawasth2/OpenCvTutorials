import cv2
import numpy as np

img1 = cv2.imread('watch.jpg')
img2 = cv2.imread('gears.png')


# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# Adds together the two images some how
# add = img1 + img2

# This one adds the pixel values for each individually
# Max is 255,255,255 so you will get a lot of white as a result
# add = cv2.add(img1, img2)

# add images with the weight that is next to it
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.7, 0)
# cv2.imshow('add', weighted)

rows, cols, channels = img1.shape
roi = img2[0:rows][0:cols]

# converts img1 to a grayed out version of itself
img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# ret not used. mask is the new image with all pixel values 
# greater than 220 converted to 255 and everything below turned into 0
# Then it inverts the black and white
ret,mask = cv2.threshold(img1gray, 220, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('mask',mask)

# Goes through the picture
# The black area of the mask will be black,
#  the white area is colored in
# bitwise is low level logical operation that checks the pixel values
mask_invis = cv2.bitwise_not(mask)
# cv2.imshow("in", mask_invis)

# Goes through the picture
# The black area of the mask will be black,
# the white area is colored in
# This removes the mask invis from the roi in img 2 that we are editing in currently
img2_bg = cv2.bitwise_and(roi, roi, mask = mask_invis)
# cv2.imshow('im2', img2_bg)

# This gets the region of the mask from the actual image as color
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
# cv2.imshow('im1', img1_fg)

# This combines the two background and foreground images and overlays it over 
# the part of the image that we wish to overwrite with our new image part
dst = cv2.add(img2_bg, img1_fg)
img2[0:rows][0:cols] = dst

cv2.imshow("res", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()