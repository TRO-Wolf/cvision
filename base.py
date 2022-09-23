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

im_list = [gray_img, color_img, lowcon_img, highcon_img]


def shape_it(image):
    return image.reshape(-1, 1)

def organize_data(image):
    n = shape_it(image)
    base_data = pd.DataFrame(n)
    counts_data = base_data.value_counts()
    data = pd.DataFrame(counts_data)
    data.sort_index(inplace=True)
    data.rename(columns={0:"counts"}, inplace=True)
    data['Probability'] = data['counts'] / data['counts'].sum()
    data['Intensity'] = reduce(lambda x, y: x + y, data.index)

    return data




'''
n = gray_img.reshape(-1, 1)

base_data = pd.DataFrame(n)
counts_data = base_data.value_counts()
data = pd.DataFrame(counts_data)

data.sort_index(inplace=True)
data.rename(columns={0:"counts"}, inplace=True)
data['Probability'] = data['counts'] / data['counts'].sum()
'''




plt.imshow(gray_img)

im_data = organize_data(gray_img)


#data.value_counts().hist(bins=30)
#p = data.value_counts().hist(bins=30)

if __name__== "__main__":
    #print(data)
    print(im_data)
    print("The mean of the the image is {}".format(im_data['Probability'].mean()))
    print("The variance of the image is {}".format(im_data['Probability'].var()))

    plt.show()

