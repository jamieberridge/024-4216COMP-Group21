
# Nursery Affect on Grades

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets and store them
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

nurseriesPor = por.groupby(by = 'nursery')[['G1', 'G2', 'G3']].mean()
nurseriesMaths = maths.groupby(by = 'nursery')[['G1', 'G2', 'G3']].mean()

# Setting size of the window
plt.figure(figsize=(10, 5))

# Plot for Portuguese
plt.subplot(1, 2, 1)
plt.plot(nurseriesPor.columns, nurseriesPor.loc['yes'], alpha=0.7)
plt.plot(nurseriesPor.columns, nurseriesPor.loc['no'], alpha=0.7)
plt.title('Nursery vs Grade (Portuguese)')
plt.ylabel('Average Grade')
plt.xlabel('Grade')
plt.grid(True)
plt.legend(["Attended Nursery", "Did not attend Nursery"], loc='lower center')

# Plot for Maths
plt.subplot(1, 2, 2)
plt.plot(nurseriesMaths.columns, nurseriesMaths.loc['yes'], alpha=0.7)
plt.plot(nurseriesMaths.columns, nurseriesMaths.loc['no'], alpha=0.7)
plt.title('Nursery vs Grade (Maths)')
plt.ylabel('Average Grade')
plt.xlabel('Grade')
plt.grid(True)
plt.legend(["Attended Nursery", "Did not attend Nursery"], loc='lower center')

# Bonus: Show if attending nursery affects the students prospects of going to higher education
nurseriesHigherEduPor = por.groupby(by = 'nursery')['higher'].value_counts()
nurseriesHigherEduMaths = maths.groupby(by = 'nursery')['higher'].value_counts()
merged = pd.concat([nurseriesHigherEduPor, nurseriesHigherEduMaths], axis=1)
merged.columns = ['Portuguese', 'Maths']
merged.plot(kind='bar')
plt.title('(Bonus) Students attending nursery and wanting to go to higher education')
plt.ylabel('Number of students')
plt.xlabel('Attended Nursery and wants to go to higher education')
plt.xticks([0, 1, 2 , 3], ['No Nursery No Higher ed', 'Yes nursery no higher ed', 'Yes Nursery Yes Higher ed', 'No Nursery Yes Higher ed'])
plt.legend(["Portuguese", "Maths"], loc='upper right')

# Configure the graph
plt.tight_layout()

# Show the graph
plt.show()