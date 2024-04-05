import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def boxplot(subject, ax, title):
    # Get data for male students
    maleStudentMaleGuardian = subject[(subject['sex'] == 'M') & (subject['guardian'] == 'father')]
    maleStudentFemaleGuardian = subject[(subject['sex'] == 'M') & (subject['guardian'] == 'mother')]

    # Get data for female students
    femaleStudentMaleGuardian = subject[(subject['sex'] == 'F') & (subject['guardian'] == 'father')]
    femaleStudentFemaleGuardian = subject[(subject['sex'] == 'F') & (subject['guardian'] == 'mother')]

    # Combine data for box plot
    boxplotData = [maleStudentMaleGuardian['G3'], maleStudentFemaleGuardian['G3'], femaleStudentMaleGuardian['G3'], femaleStudentFemaleGuardian['G3']]

    # Create box plot thats filled with a lightblue colour and is horizontal
    ax.boxplot(boxplotData, patch_artist=True, labels=["Male Student \nMale Guardian", "Male Student \nFemale Guardian", "Female Student \nMale Guardian", "Female Student \nFemale Guardian"], vert=False, boxprops=dict(facecolor="lightblue"))

    # Create title and x & y axis 
    ax.set_xlabel("Final Grade (G3)")
    ax.set_ylabel("Gender of Student and Guardian")
    ax.set_title(title)

    # Add text next to the median values to show what they're
    for i, data in enumerate(boxplotData):
        ax.text(np.median(data) + 0.1, i + 1, f"{np.median(data):.1f}", va='center', ha='left', color='red')

    # Make sure the scale is correct for the data
    ax.set_xlim(0, 22)


# Load the data from the CSV file
por = pd.read_csv('por2.csv')
mat = pd.read_csv('mat2.csv')

# Create two subplots on the same figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# Call the function twice one for each csv file
boxplot(por, ax1, "Distribution of Final Grades in Portuguese by Student Gender and Guardian Gender")
boxplot(mat, ax2, "Distribution of Final Grades in Maths by Student Gender and Guardian Gender")

# Set a common title for the entire figure
plt.suptitle("Comparison of Final Grades by Student Gender and Guardian Gender", fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()