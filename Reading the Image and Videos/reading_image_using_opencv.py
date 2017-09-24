# This program is used to read image from the directory using OpenCV

#Import opencv
import cv2
import matplotlib.pyplot as plt


# Reading the Image
# cv2.imread(filename, [,flags])
img = cv2.imread('../images/cottage.jpg')

# Displaying the Image
# OpenCV defaultly read image in the form of BGR
# cv2.cvtColor will convert BGR colored image to RGB
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
