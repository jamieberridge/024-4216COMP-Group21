import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files 
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Combine the datasets
combined = pd.concat([por, maths])

# Create the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(10, 6), sharey=True)

# Plot the boxplots for each gender
for i, gender in enumerate(['F', 'M']):
    # Filter data by gender and if in a relationship
    data = combined[combined['sex'] == gender]
    notInRelationship = data[data['romantic'] == 'no']['G3']
    inRelationship = data[data['romantic'] == 'yes']['G3']
    
    # Add the boxes
    axs[i].boxplot([notInRelationship, inRelationship], vert=False, labels=["Not in a Relationship", "In a Relationship"])
    axs[i].set_xlabel("Final Grade (G3)")
    # Set title dependent on the gender
    if gender == 'F':
        axs[i].set_title("Gender: Female")
    else:
        axs[i].set_title("Gender: Male")

# Set a title for the entire figure
plt.suptitle("Comparison between how a relationship affects grades of each gender", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
