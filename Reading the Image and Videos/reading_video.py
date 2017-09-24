# This program is used to read video using webcam

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the Video
# 0 specifies the default webcam of your system
cap = cv2.VideoCapture(0)

# True specifies the is capture is opened or not
while True:
    # cap.read() returns the isCapOpened value True and video frame
    ret, frame = cap.read()

    # imshow will display the video
    cv2.imshow('frame', frame)

    # Kills the video recording when we press q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releases the capture 
# Never forget to release the capture
cap.release()
cv2.destroyAllWindows()