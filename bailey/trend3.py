
#Romantic Relationships and parental cohabitation status

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the datasets into pandas DataFrames
portuguese = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')


# Group data by 'Pstatus' and 'romantic', and count the frequency of each combination
grouped_data = maths.groupby(['Pstatus', 'romantic']).size().unstack()

# Plot the grouped bar chart
plt.figure(figsize=(10, 6))
bars = grouped_data.plot(kind='bar', width=0.8, alpha=0.8)

# Add labels and title
plt.xlabel('Parental Cohabitation Status')
plt.ylabel('Number of Students')
plt.title('Relationship Status by Parental Cohabitation')

# Add legend
plt.legend(title='Romantic Relationship', labels=['Not in Relationship', 'In Relationship'], loc='upper left')

# Add grid
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for i in range(len(grouped_data.columns)):
    for j, value in enumerate(grouped_data.iloc[:, i]):
        plt.text(j, value + 5, str(value), ha='center', va='bottom')


# Add annotation on top right
plt.text(1, 0.95, 'T = Together\nA = Apart', transform=plt.gca().transAxes, fontsize=10, ha='right', va='top', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.tight_layout()
plt.show()
