import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # A laplacian gradient of a frame
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # does gradient in x direction
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    # does gradient in y direction
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
    # inbuilt cv2 edge detection, larger param2,3 the less
    # edges are shown ie only the more important ones are picked up
    edges = cv2.Canny(frame, 100, 100)


    # cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()