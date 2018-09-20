import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

print(img.shape)

# Draws line, takes image to draw on, start coordinate, end coordinate, color and line width
cv2.line(img, (0, 0), (300, 300), (0,0,0), 15)

# Draws rectangle on image(param1) with top left corner at param2 and with bottom right corner
# at param3 with color param4 and line width param5
cv2.rectangle(img, (100,100), (400, 400), (255, 0, 0), 5)

# Draws circle on image(param1) with center param2, radius param3, color param4 and
# linewidth param5. If linewidth is negative then it fills the shape
cv2.circle(img, (300, 300), 100, (0,0, 255), -1)

# Draw a polygon with pts at following locations and data type is last param
pts = np.array([[300, 5], [500, 200], [ 400, 400], [200, 400], [100,200]], np.int32)

## Reshape the array to 1 by 2, not needed
#pts = pts.Reshape((-1, 1, 2))

# Draw on image, with vertices param2, boolean whether to connect last point to first and color
cv2.polylines(img, [pts], True, (255, 255, 0), 15)

#Writing
font = cv2.FONT_HERSHEY_SIMPLEX
#write on image, says param2, starts at param3, font is param4, param5 is fontsize, param6 is color
#param7 is spacing, param8 is attempted anti-aliasing
cv2.putText(img, 'OpenCV Tuts!', (0, 130), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
