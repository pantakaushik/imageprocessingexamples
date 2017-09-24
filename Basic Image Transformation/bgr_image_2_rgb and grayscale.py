# This program will convert a sample BGR image to RGB image and Displaying it

import cv2
import matplotlib.pyplot as plt

# Read Image
# here the img variable will have BGR image
img = cv2.imread('../images/cottage.jpg')

# cvtColor will convert image color
# cv2.COLOR_BGR2RGB will convert BGR image to RGB
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.COLOR_RGB2GRAY will convert RGB image to Grayscale(Black and White)
img_GRAY = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)



cv2.imwrite('../images/cottage_RGB.jpg', img)
cv2.imwrite('../images/cottage_BGR.jpg', img_RGB)
cv2.imwrite('../images/cottage_GRAY.jpg', img_GRAY)


