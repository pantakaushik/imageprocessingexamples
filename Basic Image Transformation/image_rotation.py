# This program will rotate the input image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading of Image
img = cv2.imread('../images/cottage.jpg',0)

# Getting rows and columns of image using img.shape
rows, cols = img.shape

# Rotating the image using getRotationMatrix2D where we pass center of rotation, angle and zooming level
rot_img = cv2.getRotationMatrix2D((0,0),10,1.0)

# Finally we wrapAffine the image
final_image = cv2.warpAffine(img, rot_img, (cols,rows))


# Plotting of Image
plt.imshow(final_image)

plt.show()