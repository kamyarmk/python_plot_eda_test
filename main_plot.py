import os
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv('data.csv')

avrage_time_spent = df.groupby('gender')['time_spent'].mean()

avrage_time_spent.plot(kind='bar', title='Average Time Spent by Gender', xlabel='Gender', ylabel='Time Spent by Gender')


plt.show()