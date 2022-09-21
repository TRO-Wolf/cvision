from unicodedata import name
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 as cv


gray_img = cv.imread("grayscaledog.png")
color_img = cv.imread("colordog.jpg")

lowcon_img = cv.imread("lowcontrast.jpg")
highcon_img = cv.imread("highcontrast.jpeg")


n = gray_img.reshape(-1, 1)

base_data = pd.DataFrame(n)
counts_data = base_data.value_counts()
data = pd.DataFrame(counts_data)

data.sort_index(inplace=True)
data.rename(columns={0:"counts"}, inplace=True)

data['Probability'] = data['counts'] / data['counts'].sum()




#data.value_counts().hist(bins=30)
#p = data.value_counts().hist(bins=30)

if __name__== "__main__":
    print(data)

