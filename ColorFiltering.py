import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# while video is running
while True:
    # gets frame of video, first part doesn't really matter
    _, frame = cap.read()

    #hue separation value: CONVERSion
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # hsv is hue, sat, value
    lower_orange = np.array([0,100, 100])
    upper_orange = np.array([50,255,255])

    # all hues in image in range of param2, param3
    # if in range, it is white
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # if in white then keep color
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # wait for escape button then break loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
