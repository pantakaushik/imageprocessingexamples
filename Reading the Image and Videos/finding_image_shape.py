# This program will fin the shape of image that we have read
import cv2


# Reading the Image
img = cv2.imread('../images/cottage.jpg')

# Displaying the Shape of RGB or BGR images
# It will return 3 values in tuple providing image height, width and Color Combination
# In case of BGR or RGB image , the number of color used is 3
print(img.shape)

# Displaying the shape of GrayScale image
# It will return only two values i.e. image height and width
# Since gray scale image have no color used it it so the tuple will be of length 2
img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_Gray.shape)