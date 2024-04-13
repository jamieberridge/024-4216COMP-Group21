
# Heath vs Grade

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Group the data by health for each subject
mathsHigherEdu = maths.groupby(by = 'health')['G3'].median()
porHigherEdu = por.groupby(by = 'health')['G3'].median()
#Median is used to avoid outliers -- Less people are going to be in the middle rather than the super healthy or super unhealthy

# Setting size of the window
plt.figure(figsize=(10, 5))

# Plot for Maths
plt.subplot(1, 2, 1)
plt.scatter(mathsHigherEdu.index, mathsHigherEdu.values, alpha=0.7)
plt.title('Health vs Grade (Maths)')
plt.ylabel('Average Grade')
plt.xlabel('Health')
plt.grid(True)

# Plot for Portuguese
plt.subplot(1, 2, 2)
plt.scatter(porHigherEdu.index, porHigherEdu.values, alpha=0.7)
plt.title('Health vs Grade (Portuguese)')
plt.ylabel('Average Grade')
plt.xlabel('Health')
plt.grid(True)

# Show the graph
plt.show()