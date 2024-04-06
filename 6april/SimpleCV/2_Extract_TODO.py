import cv2
import numpy as np

# TODO open handle to video file

# TODO font for drawing text 

# player color range in HSV
playerLo    = np.array([25,50,50])
playerHi    = np.array([35,255,255])

# top of purple floor color range in HSV
floorLo     = np.array([150,50,50])
floorHi     = np.array([160,255,255])

# TODO read the stream frame by frame
while False:
    # TODO read frame
    
    # TODO change color spaces from RGB to HSV
    
    # TODO mask out the player color range
    
    # TODO caculate the center via moments
    # TODO get moments from player mask
    M = "TODO"
    if M["m00"] != 0:
        # this part directly taken from docs
        # the mathematically inclined amongus
        # might wanna go learn around moments (optional)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(cX, cY)
        # TODO draw some cute graphics

    # TODO mask out the floor color range
    floorMask = cv2.inRange(hsv, floorLo, floorHi)

    # TODO imshow some intermediate frames to see whats going on

    # early termination condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# TODO cleanup