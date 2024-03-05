import os
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv('data.csv')

ages = [10, 20, 30, 40, 50]
cols = ['location', 'interests', 'platform', 'profession']

# Sort the Values by their age
sorted_by_age = df.sort_values(by='age')

# creating the History plot 
sorted_by_age['age'].plot(kind='hist', bins=100, color='orange')

# Create a new figure and set up subplots
fig, axes = plt.subplots(nrows=len(cols), ncols=5, figsize=(15, 15))

# The Function to make a chart based on the ages an the columns we are looking for
def group_by_age(x, y, col, ax):
    age_init= df[(df['age'] >= x) & (df['age'] <= y)]
    return age_init.groupby(col)['time_spent'].sum().plot(kind = 'bar', title=f"({x} - {y})Age {col}", xlabel=col , ylabel='Time Spent', ax=ax, grid=True)

# Running each type of stats we want to categorise by age
for i, col in enumerate(cols):
    for j, age in enumerate(ages):
        group_by_age(age, age + 10, col, axes[i, j])
        
plt.show()