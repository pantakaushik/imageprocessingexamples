# This program will scale the image

import cv2
import matplotlib.pyplot as plt
import numpy as np


# Reading the image
img = cv2.imread('../images/cottage.jpg')

# Finding the Height and Width of image
height, width = img.shape[:2]

# Resizing the image using interpolations=INTER_CUBIC
resize_image = cv2.resize(img, (5*width,5*height), interpolation = cv2.INTER_CUBIC)


# Plotting the image
# plt.imshow(resize_image)
# plt.show()
cv2.imshow('img',resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()