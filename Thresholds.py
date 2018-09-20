import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
# cv2.imshow('origin', img)

# convert all values above 12 to white
# Will be colored image because you are still working with BGR colors
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold', threshold)

# Converts BGR to Grayscale
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Does same threshold conversion
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold2', threshold2)

# Gauss Adaptive Threshold
# image, value to scale to, type of adaptative threshold,
#  normal threshold, the BxB amount of pixels B that you want to scan,
#  constant subtracted from the weight of the pixels
gauss = cv2.adaptiveThreshold(grayscaled, 255,
 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('gauss', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()