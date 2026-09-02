import stat
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("Bestsellers with categories.csv")
data.head

median_User_Rating = np.median(data['User Rating'])
print("Median value of User Rating -", median_User_Rating)

mode_User_Rating = data['User Rating']
print("Mode value of User Rating -", mode_User_Rating)

mean_User_Rating = np.mean(data['User Rating'])
print("Mean value of User Rating -", mean_User_Rating)

median_Price = np.median(data['Price'])
print("Median value of Price -", median_Price)

mean_Price = np.mean(data['Price'])
print("Mean value of Price -", mean_Price)

mode_Price = data['Price']
print("Mode value of Price -", mode_Price)

median_Reviews= np.median(data['Reviews'])
print("Median value of Reviews -", median_Reviews)

mean_Reviews= np.mean(data['Reviews'])
print("Mean value of Reviews -", mean_Reviews)

mode_Reviews=  data['Reviews']
print("Mode value of Reviews -", mode_Reviews)
