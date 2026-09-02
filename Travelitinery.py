import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Weather Dataset.csv")
data.head(5)
data.info()
data.isnull().sum()

mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is :", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("Var Temperature is :", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation's Temperature is :", standard_deviation_temp)

for i in range(1, 13):
    month = data.loc[data["month"] == i]["Temperature (C)"]
    print("For month "+str(1))
    print("Mean Temperature is "+str(np.mean(month)))
    print("Standard Deviation Temperature is "+str(np.mean(month))+"\n")