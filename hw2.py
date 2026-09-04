import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("Bestsellers with categories.csv")
data.head(5)
data.isnull().sum()

variance_User_Rating = np.var(data['User Rating'])
print("Variance value of User Rating -", variance_User_Rating)

std_User_Rating = np.std(data['User Rating'])
print("Standard Deviation value of User Rating -", std_User_Rating)

variance_Price = np.var(data['Price'])
print("Variance value of Price -", variance_Price)

std_Price = np.std(data['Price'])
print("Standard Deviation value of Price -", std_Price)


plt.hist(data["User Rating"], bins=10)

plt.title("Distribution of User Rating")
plt.xlabel("User Rating")
plt.ylabel("Number of Books")

plt.show()

plt.hist(data["Price"], bins=10)

plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.show()