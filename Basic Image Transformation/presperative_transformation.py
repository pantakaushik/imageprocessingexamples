# This transformation leads to change in the point of view of the image. The straight lines remain as it is. 
# For this transformation we need 4 points from the source and output image of which 3 should be non-collinear to define a plane. 
# From these points we define a 3×3 matrix using cv2.getPerspectiveTransform and pass the resulting matrix into cv2.warpPerspective.

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Reading the Image
img = cv2.imread('../images/cottage.jpg')
rows,cols,ch = img.shape


pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()