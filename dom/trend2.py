
#Free Time on Grades

import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets then store them into variables
maths = pd.read_csv('mat2.csv')
por = pd.read_csv('por2.csv')
maths = maths[['G3', 'freetime']]
por = por[['G3', 'freetime']]

# Setting size of the window
plt.figure(figsize=(10, 5))
# Produces the scatter plot
plt.subplot(1, 2, 1)
plt.scatter(maths['freetime'], maths['G3'], alpha=0.7)
plt.title('Maths')
plt.xlabel('Freetime')
plt.ylabel('Grade')
plt.grid(True)
# Creating the scatter plot for Portuguese using subplot to compare with Maths
plt.subplot(1, 2, 2)
plt.scatter(por['freetime'], por['G3'], alpha=0.7)
plt.title('Portuguese')
plt.xlabel('Freetime')
plt.ylabel('Grade')
plt.grid(True)

# Show the graph
plt.show()