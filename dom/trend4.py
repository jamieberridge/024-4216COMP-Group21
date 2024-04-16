
# Failures of students vs Family Support

import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets and store them
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Group the datasets by familysupport and then find the mean
mathsFailuresByFamsup = maths.groupby('famsup',)['failures'].mean()
porFailuresByFamsup = por.groupby('famsup',)['failures'].mean()

# Concatinate both groups of datasets
FailuresByFamsup = pd.concat([mathsFailuresByFamsup, porFailuresByFamsup], axis=0)
plt.figure(figsize=(10, 7))

# Make a bar chart FailuresByInternet
plot = FailuresByFamsup.plot(kind='bar', xlabel='Family Support', ylabel='Average Failures', title='Average Failures compared to Family Support', width = 0.8)
plot.set_xticklabels(["Maths \nNo Family Support", "Maths \nActive Family Support", "Portuguese \nNo Family Support", "Portuguese \nActive Family Support"])
# Add a grid to improve visual clarity
plot.grid(True)

# Rotate the labels on the x axis
plt.xticks(rotation=0)
# Open the window
plt.show()