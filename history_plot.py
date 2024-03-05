import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv('data.csv')

cols = ['income', 'time_spent', 'age']

# Sort the Values by their age
sorted_by_age = df.sort_values(by='age')

# Create a new figure and set up subplots
fig, axes = plt.subplots(nrows=1, ncols=len(cols), figsize=(30, 5))

# The Function to make a chart based on the ages an the columns we are looking for
def group_by_age(col, ax):
    return sns.histplot(data=df, kde=True, x=col , ax=ax)

# Running each type of stats we want to categorise by age
for i, col in enumerate(cols):
    group_by_age(col, axes[i])
    axes[i].set_ylabel('Frequency')  # Adjust y-axis label

plt.show()