import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img1 = cv2.imread('../ExcursionsIntoMlAndAdvLinAlg/cornercast2.png', 0)
img2 = cv2.imread('../ExcursionsIntoMlAndAdvLinAlg/container.jpg', 0)

# detector of similarities
orb = cv2.ORB_create()

# keypoint and descriptors of each image
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# find keypoints and descriptors now
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# find and sort matches based on distance/accuracy/confidence
matches = bf.match(des1, des2)
# most likely to leas likely to match
matches = sorted(matches, key = lambda x:x.distance)

# shows the first 10 matches of keypoints in each image
img4 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:5], None, flags = 2)


def most_match_finder(img, kp, matches):
    best_x = 0
    best_y = 0
    max_match = 0
    range_ = 100
    matches = sorted(matches, key = lambda x:x.distance)
    for y in range(0, len(img), range_):
        for x in range(0, len(img[y]), range_):
            curr_match = 0
            for m in matches[:10]:
                loc1, loc2 = kp[m.trainIdx].pt
                cv2.circle(img, ( int(math.floor(loc1)), int(math.floor(loc2)) ), 20, 0, -1)
                if loc1 >= x and loc1 <= x + range_ and loc2 >= y and loc2 <= y + range_:
                    curr_match += 1
            if curr_match > max_match:
                best_x = x
                best_y = y
                max_match = curr_match
    cv2.rectangle(img, (best_x, best_y), (best_x + range_, best_y + range_), 0, 5) 
    return best_x, best_y, range_


most_match_finder(img2, kp2, matches)
cv2.imshow('img2' ,img2)
cv2.waitKey()
cv2.destroyAllWindows()



