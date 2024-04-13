
# Attendances Effect on Grade

import pandas as pd
import matplotlib.pyplot as plt

# Read the attendance data from mat2.csv and por2.csv
maths = pd.read_csv('mat2.csv')
por = pd.read_csv('por2.csv')

maths = maths[['G1', 'G2', 'G3', 'absences']]
por = por[['G1', 'G2', 'G3', 'absences']]

# Setting size of the window
plt.figure(figsize=(10, 5))
# Creating the scatter plot for maths using subplot to compare with Portuguese
plt.subplot(1, 2, 1)
plt.scatter(maths['absences'], maths['G3'], alpha=0.7)
plt.title('Maths')
plt.xlabel('Absences')
plt.ylabel('Final Grade')
plt.grid(True)
# Creating the scatter plot for Portuguese using subplot to compare with Maths
plt.subplot(1, 2, 2)
plt.scatter(por['absences'], por['G3'], alpha=0.7)
plt.title('Portuguese')
plt.xlabel('Absences')
plt.ylabel('Final Grade')
plt.grid(True)

# Show the graph
plt.show()