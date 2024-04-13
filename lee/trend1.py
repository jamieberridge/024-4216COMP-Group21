
# School Support vs Family Support vs Paid Classes

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets and store them
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

famSupPor = por.groupby(by = 'famsup')['G3'].mean()
famSupMaths = maths.groupby(by = 'famsup')['G3'].mean()
schoolSupPor = por.groupby(by = 'schoolsup')['G3'].mean()
schoolSupMaths = maths.groupby(by = 'schoolsup')['G3'].mean()
paidPor = por.groupby(by = 'paid')['G3'].mean()
paidMaths = maths.groupby(by = 'paid')['G3'].mean()

# Setting size of the window
plt.figure(figsize=(10, 5))

# Plot for Portuguese
plt.subplot(1, 2, 1)
plt.scatter(famSupPor.index, famSupPor.values, alpha=0.7)
plt.scatter(schoolSupPor.index, schoolSupPor.values, alpha=0.7)
plt.scatter(paidPor.index, paidPor.values, alpha=0.7)
plt.title('Family/school support vs Paid classes (Portuguese)')
plt.ylabel('Average Grade')
plt.xlabel('Support Type')
plt.legend(["Family Support", "School Support", "Paid"], loc='lower center')

# Plot for Maths
plt.subplot(1, 2, 2)
plt.scatter(famSupMaths.index, famSupMaths.values, alpha=0.7)
plt.scatter(schoolSupMaths.index, schoolSupMaths.values, alpha=0.7)
plt.scatter(paidMaths.index, paidMaths.values, alpha=0.7)
plt.title('Family/school support vs Paid classes (Maths)')
plt.ylabel('Average Grade')
plt.xlabel('Support Type')
plt.legend(["Family Support", "School Support", "Paid"], loc='lower center')

# Show the graph
plt.show()