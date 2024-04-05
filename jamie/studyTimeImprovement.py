import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Combine the two datasets
mergedSubjects = pd.concat([por, maths])

# Calculate grade improvement
mergedSubjects['gradeDifference'] = mergedSubjects['G3'] - mergedSubjects['G1']

# Create a pivot table to find the relationship between study time and grade improvement
pivotTable = mergedSubjects.pivot_table(index='studytime', columns='gradeDifference', values='G3', aggfunc='count')

# Create a dictionary to map the 1-4 number given in the data to a real world number
studyTimeDictionary = {
    1: '<2 hours',
    2: '2-5 hours',
    3: '5-10 hours',
    4: '10 hours<'
    }

# Plotting the figure size
plt.figure(figsize=(10, 6))
# Plotting the heatmap with seaborn
sns.heatmap(pivotTable, cmap='coolwarm', annot=True, fmt='g')
# Adding labels for the title and the x & y axis
plt.title('Relationship Between Study Time and Grade Improvement (Combined Data)')
plt.xlabel('Grade Improvement from G1 to G3')
plt.ylabel('Weekly Study Time')
# Setting the y axis labels to the ones they correspond to in the directionary
plt.yticks(ticks=[0, 1, 2, 3], labels=[studyTimeDictionary[i] for i in range(1, 5)])
# Invert the y axis to increase readability of the data
plt.gca().invert_yaxis() 
plt.show()
