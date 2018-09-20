import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
# shape returns height X width X other dimensions
# the current thing returns only height and width
# and makes them all 0s
mask = np.zeros(img.shape[:2], np.uint8)

# basically the same thing
# creates a 1x65 array of 0's that are float64
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

# first two are top left, last two is size
rect = (161, 79, 150, 150)

#takes image, mask, rectange, background, foreground, iterations to run, and model
#it adjusts mouse to consider different parts of the picture as foreground and background
#0,2 in mask will now be background. Odds will be foreground
# you can replace rect with NONE and INIT_WITH_MASK in order to specify locations with certainty to be foreground and background
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5 , cv2.GC_INIT_WITH_RECT)
# newmask is the mask image I manually labelled
# newmask = cv2.imread('newmask.png',0)
#
# # wherever it is marked white (sure foreground), change mask=1
# # wherever it is marked black (sure background), change mask=0
# mask[newmask == 0] = 0
# mask[newmask == 255] = 1
# mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
# converts 0,2 to 0 and 1,3 to 1 so differentiates between foreground and background
mask2 = np.where((mask == 2) | (mask ==0), 0, 1).astype('uint8')
# fancy slicing multiplies each pixel by the assigned 0,1 values 
# Then background turns black and foreground remains the same color
img = img * mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()