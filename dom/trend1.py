
# Failures of students and Internet Access

import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets then store them into variables
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Group the datasets by internet status and then find the mean
mathsFailuresByInternet = maths.groupby('internet',)['failures'].mean()
porFailuresByInternet = por.groupby('internet',)['failures'].mean()

# Concatinate both groups of datasets
FailuresByInternet = pd.concat([mathsFailuresByInternet, porFailuresByInternet], axis=0)

# Made the window the appropriate size to fit the bar charts
plt.figure(figsize=(10, 7))

# Make a bar chart FailuresByInternet
plot = FailuresByInternet.plot(kind='bar', xlabel='Internet Access', ylabel='Average Failures', title='Average Failures and Internet Access', width = 0.8)
plot.set_xticklabels(["Maths \nInternet Access", "Maths \nNo Internet Access", "Portuguese \nInternet Access", "Portuguese \nNo Internet Access"])
# Add a grid to improve visual clarity
plot.grid(True)

#  Set labels for the top of each bar to show their y value
for i, grade in enumerate(FailuresByInternet):
    plot.text(i, grade + 0.1, f"{grade:.2f}", ha='center', va='bottom')

# Rotate the labels on the x axis
plt.xticks(rotation=0)
# Open the window
plt.show()