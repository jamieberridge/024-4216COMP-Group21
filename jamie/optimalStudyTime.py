import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets and store them
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Group both datasets by study time
mathsGradesByStudyTime = maths.groupby('studytime',)['G3']
porGradesByStudyTime = por.groupby('studytime',)['G3']

# Plotting the line graph for maths grades
plt.plot(mathsGradesByStudyTime.mean(), label="Maths", marker='o')
# Plotting the line graph for Portuguese grades
plt.plot(porGradesByStudyTime.mean(), label="Portuguese", marker='o')

# Plotting line to show optimal study time
plt.axvline(x=3.0, color='r', linestyle='--', label="Optimal Study Time")

# Adding labels and title
plt.xlabel("Study Time (hours per week)")
plt.ylabel("Average Grades")
plt.title("Average Grades by Study Time")

# Adding legend
plt.legend()
# Adding the grade boundries text box
plt.text(4.11, 9.98, "Grade Boundaries:\n18 to 20 - Excellent\n16 and 17 - Very good\n14 and 15 - Good\n10 to 13 - Pass\n0 to 9 - Fail", bbox=dict(facecolor='white', alpha=0.5), ha= 'right')

# Displaying the graph
plt.show()