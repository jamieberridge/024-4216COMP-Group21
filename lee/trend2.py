
# Ages and grades

import pandas as pd
import matplotlib.pyplot as plt
#line graph to compare age and grade -- 1 line for each age. Y axis is grade/score and X axis is G1/G2/G3


# Read the CSV files
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Separate the dataframes
G1AgeMaths = maths.groupby(by='age')['G1'].mean()
G2AgeMaths = maths.groupby(by='age')['G2'].mean()
G3AgeMaths = maths.groupby(by='age')['G3'].mean()

G1AgePor = por.groupby(by='age')['G1'].mean()
G2AgePor = por.groupby(by='age')['G2'].mean()
G3AgePor = por.groupby(by='age')['G3'].mean()

plt.figure(figsize=(10, 5))
# Plotting the data for maths
plt.subplot(1, 2, 1)
plt.plot(G1AgeMaths.index, G1AgeMaths.values, alpha=0.75)
plt.plot(G2AgeMaths.index, G2AgeMaths.values, alpha=0.75)
plt.plot(G3AgeMaths.index, G3AgeMaths.values, alpha=0.75)
plt.title('Age vs Grade (Maths)')
plt.ylabel('Average score')
plt.xlabel('Age')
plt.grid(True)
plt.xticks(G1AgeMaths.index, [f"{age} Y.O." for age in G1AgeMaths.index])
plt.legend(["First Grade", "Second Grade", "Third Grade"], loc='lower left')

# Plotting the data for Portuguese
plt.subplot(1, 2, 2)
plt.plot(G1AgePor.index, G1AgePor.values, alpha=0.75)
plt.plot(G2AgePor.index, G2AgePor.values, alpha=0.75)
plt.plot(G3AgePor.index, G3AgePor.values, alpha=0.75)
plt.title('Age vs Grade (Portuguese)')
plt.ylabel('Average score')
plt.xlabel('Age')
plt.grid(True)
plt.xticks(G1AgePor.index, [f"{age} Y.O." for age in G1AgePor.index])
plt.legend(["First Grade", "Second Grade", "Third Grade"], loc='lower left')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the graph
plt.show()


# Show the graph
plt.show()