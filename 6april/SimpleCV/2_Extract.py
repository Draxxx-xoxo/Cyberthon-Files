import cv2
import numpy as np

# open handle to video file
stream = cv2.VideoCapture('kultisti.mp4')

# font for drawing text 
font = cv2.FONT_HERSHEY_SIMPLEX

# player color range in HSV
playerLo    = np.array([25,50,50])
playerHi    = np.array([35,255,255])

# top of purple floor color range in HSV
floorLo     = np.array([150,50,50])
floorHi     = np.array([160,255,255])

# read the stream frame by frame
while(stream.isOpened()):
    # read frame
    ret, frame = stream.read()
    
    # change color spaces from RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    playerMask = cv2.inRange(hsv, playerLo, playerHi)

    M = cv2.moments(playerMask)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(cX, cY)
        frame = cv2.putText(frame, f'player = ({cX}, {cY})', (0,40), font, 1, (255,0,0), 2, cv2.LINE_AA)
        frame = cv2.circle(frame, (cX, cY), 20, (0,0,255), 2)

    floorMask = cv2.inRange(hsv, floorLo, floorHi)

    cv2.imshow('hsv', hsv)
    cv2.imshow('playerMask', playerMask)
    cv2.imshow('floorMask', floorMask)
    cv2.imshow('frame', frame)

    # early termination condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()