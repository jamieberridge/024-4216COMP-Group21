
# Parental Education and Student Performance

import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
portuguese = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

def plot(subject, ax, title):
    # Calculate mean parental education
    #  0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education
    subject['meanParentEducation'] = (subject['Medu'] + subject['Fedu']) / 2

    # Drop anomalous data
    if title == 'Maths':
        subject = subject[subject.index != 171]

    # Group data by mean parental education and calculate average grades
    averageGradeByGuardianEducation = subject.groupby('meanParentEducation')[['G1', 'G2', 'G3']].mean()

    # Plot the line graph
    averageGradeByGuardianEducation.plot(marker='o', figsize=(10, 6), ax=ax)
    # Create title and x & y axis
    ax.set_title(title)
    ax.set_xlabel("Mean Parental Education")
    ax.set_ylabel("Average Grade")
    ax.grid(True)

# Create a figure and two axes objects 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Call the function to plot for each subject
plot(portuguese, ax1, 'Portuguese')
plot(maths, ax2, 'Maths')
plt.suptitle("Comparison of Mean Parental Education with Mean Grades", fontsize=16, fontweight='bold')

# Show the plots
plt.tight_layout()
plt.show()