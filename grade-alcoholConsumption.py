# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the datasets into pandas DataFrames
portuguese = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Group the 'maths' DataFrame by alcohol consumption and calculate the mean grades
alcoholToGrades = maths.groupby("Walc")["G3"].mean()

# Create a bar plot to visualize the relationship between alcohol consumption and grades
ax = alcoholToGrades.plot(kind='bar', xlabel='alcohol consumption (1 low - 5 high)', ylabel='grades',title='grade changes based on alcohol consumption')

# Add grid to the plot
ax.grid(True)

# Annotate each bar with its corresponding grade value
for i, grade in enumerate(alcoholToGrades):
    ax.text(i, grade + 0.1, f"{grade:.2f}", ha='center', va='bottom')

# Display the plot
plt.show()
