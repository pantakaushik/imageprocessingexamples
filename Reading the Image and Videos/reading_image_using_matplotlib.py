# This program is used to read image from the directory using MatPlotlib

# import Matplotlib
import matplotlib.pyplot as plt

img = plt.imread("../images/cottage.jpg")

# plotting the image
plt.imshow(img)
plt.show()