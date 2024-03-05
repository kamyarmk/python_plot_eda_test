import os
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv('data.csv')

# Sort the Values by their age
sorted_by_age = df.sort_values(by='age')

# creating the History plot 
sorted_by_age['age'].plot(kind='hist', bins=100, color='orange')

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title(f"Age Distribution")
plt.grid(True)
plt.legend()
plt.xticks(rotation=90)
        
plt.show()