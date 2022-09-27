from functools import reduce
from unicodedata import name
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 as cv


gray_img = cv.imread("grayscaledog.png")
color_img = cv.imread("colordog.jpg")

lowcon_img = cv.imread("lowcontrast.jpg")
highcon_img = cv.imread("highcontrast.jpeg")


plt.imshow(gray_img)
bitwise_and = cv.bitwise_and(gray_img,)


#im_data = organize_data(gray_img)


plt.show()