
#Age distribution of students Histogram

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


# Read the datasets into pandas DataFrames
portuguese = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Calculate bin edges to align with integer tick marks on the x-axis
bin_edges = range(maths['age'].min(), maths['age'].max() + 2)

# Plot histogram with adjusted bin edges
plt.figure(figsize=(8, 6))
plt.hist(maths['age'], bins=bin_edges, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Students')
plt.grid(True)

# Add mean age line
mean_age = maths['age'].mean()
plt.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f'Mean Age: {mean_age:.2f}')
plt.legend()

plt.tight_layout()
plt.show()