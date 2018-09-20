import cv2
import numpy as np

# Using a video camera to record. 0 signifies using ur first camera, 1 ur second etc.
capture = cv2.VideoCapture(0)

# The codec that you want to use
forcc = cv2.VideoWriter_fourcc(*'XVID')
# The out file for our video, name of file, codec to use, ???, size of frame
out = cv2.VideoWriter('output.avi', forcc, 20.0, (640,480))

# infinite loop so continuously captures frames
while True:
    # You get true/false for ret
    # Then you get the current frame for curr_frame
    ret, curr_frame = capture.read()

    #Converts color to grayscale
    gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    # Adds frame to out file
    out.write(curr_frame)
    # Display gray frame
    cv2.imshow('gray frame', gray)

    # display current frame
    cv2.imshow("frame", curr_frame)

    # wait for a key to be pressed and the key value should be q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
print (curr_frame.shape)
# releases the camera so you can edit
capture.release()
# releases and saves the output file
out.release()
cv2.destroyAllWindows()
