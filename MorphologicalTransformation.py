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

    ## 2 morphological translations, erosion and dilation
    # erosion removes random colored pixels in a sea of another color
    # dilation expands a pixel's color until it cant be expanded anymore
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    ## Others are opening and closing
    # Opening removes false positives in background
    # Closing removes false negatives in subject
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    #tophat difference between input image and opening of image
    #blackhat is the difference between the closing of the input image and input image
    


    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('res', res)
    cv2.imshow('open', opening)
    cv2.imshow('close',closing)

    # wait for escape button then break loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
