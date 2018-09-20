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

    ### Averaging for smoothing
    # average of bxb pixels divided by b*b
    # not clear
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)
    # blurs and is clearer
    blur = cv2.GaussianBlur(res, (15,15), 0)
    # another type of blur
    median = cv2.medianBlur(res, 15)
    # one more blur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    # cv2.imshow('frame', frame)
    # cv2.imshow('smoothed', smoothed)
    # cv2.imshow('blur', blur)
    # cv2.imshow('median', median)
    # cv2.imshow('mask', mask)
    cv2.imshow('bilateral', bilateral)
    cv2.imshow('res', res)

    # wait for escape button then break loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
