# The following example code shifts the image by (200,100).


import cv2
import matplotlib.pyplot as plt
import numpy as np


# Reading the image
img = cv2.imread('../images/cottage.jpg',0 )

# Finding the Height and Width of image
height, width = img.shape

# Providing the translating vector
M = np.float32([[1,0,100],[0,1,50]])

# Translating the image 
# The cv2.warpAffine function takes in three arguments. 
# The first is the image. 
# Second is the transformation matrix for shifting. 
# And the third is the output size.
translate_image = cv2.warpAffine(img, M, img.shape)


# Plotting the image
plt.imshow(translate_image)
plt.show()
# cv2.imshow('img',resize_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()