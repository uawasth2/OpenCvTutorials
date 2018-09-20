import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

#pixel location gets color at location
pixel = img[55, 55]

#Changes color of pixel
img[55,55] = [0, 0, 0]

#prints color of location
print(pixel)

# Region of Image
#roi
img[100:150, 100:150] = [0, 0, 0]

#Moving image
#gets square region for squares
watch_face = img[200:400, 200:400]
img[0:200,0:200] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
