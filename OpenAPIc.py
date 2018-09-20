import cv2
import numpy as np
import matplotlib.pyplot as plt

# reads in image as grayscale
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#Other options
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

# To show image
cv2.imshow('image', img)
# param1 is name of window, param2 is image to show
cv2.waitKey(0)
# waits for any key to be pressed
cv2.destroyAllWindows()

# # Another way to show image
# plt.imshow(img, cmap='gray', interpolation= 'bicubic')
# # plots image reading in the bits as a grayscale. bicubic does something?
# plt.plot([50,100], [80, 100], 'c', linewidth = 5)
# # Choose two coordinate points and plot with color 'c' ie cyan with width 5
# plt.show()





