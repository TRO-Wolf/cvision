from functools import reduce
from unicodedata import name
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 as cv



#Question 1
gray_img = cv.imread("grayscaledog.png")
color_img = cv.imread("colordog.jpg")

lowcon_img = cv.imread("lowcontrast.jpg")
highcon_img = cv.imread("highcontrast.jpeg")

im_list = [gray_img, color_img, lowcon_img, highcon_img]



def reshape_image(image):
    return image.reshape(-1, 1)







def main_program():

    #question 2
    for i in im_list:
        new_image = cv.cvtColor(i, cv.COLOR_BGR2RGB)
        base_image_data = reshape_image(i)
        data = pd.DataFrame(base_image_data)
        data.rename(columns={0:"Intensity"}, inplace=True)


        #question 3

        #here I created a pandas dataframe based on the numpy array called base_image_data
        #I used the value counts function to calculate the total amount of each pixel in the data set

        pixel_counts = data.value_counts()
        pixel_counts.sort_index(inplace=True)
        #pixel_counts.rename(columns={0:"counts"}, inplace=True)

        #To get the probability I took the values counts data and divided by the total sum
        #as provided by the formulas in the assignemt. The total sum of Probabilites is 1

        data2 = pd.DataFrame(pixel_counts)

        data2.rename(columns={0:"counts"}, inplace=True)
        data2['Probability'] = data2['counts'] / data2['counts'].sum()



        #Question 4


        #Pandas has a function that allows you to get the skew, vairance and kurtosis of a data set
        # all in a few simple commands
        mean_intensity = data['Intensity'].mean()
        std_dev = data['Intensity'].std()
        skew = data['Intensity'].skew()
        variance = data['Intensity'].var()
        kurtosis = data['Intensity'].kurtosis()


        print("The image {}".format(i))
        print("This image has an mean intensity of {}".format(mean_intensity))
        print("The Image has a standard deviation of {}".format(std_dev))
        print("This image has a skew of {}".format(skew))
        print("This image has a variance of {}".format(variance))
        print("This image has a kurtosis of {}".format(kurtosis))

        print("     ")

        plt.imshow(new_image)
        plt.show()







if __name__== "__main__":

    main_program()
