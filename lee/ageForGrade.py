import pandas as pd
import matplotlib.pyplot as plt
#line graph to compare age and grade -- 1 line for each age. Y axis is grade/score and X axis is G1/G2/G3


# Read the CSV files
maths = pd.read_csv('mat2.csv')
por = pd.read_csv('por2.csv')

# Merge the dataframes
merged = pd.concat([maths, por])
G1Age = merged.groupby(by = 'age')['G1'].mean()
G2Age = merged.groupby(by = 'age')['G2'].mean()
G3Age = merged.groupby(by = 'age')['G3'].mean()

# Plotting the data
plt.plot(G1Age.index, G1Age.values, alpha=0.7)
plt.plot(G2Age.index, G2Age.values, alpha=0.7)
plt.plot(G3Age.index, G3Age.values, alpha=0.7)

# Configure the graph
plt.title('Age vs Grade')
plt.ylabel('Average score')
plt.xlabel('Age')
plt.grid(True)
plt.xticks(G1Age.index, [f"{age} Y.O." for age in G1Age.index])
plt.legend(["First Grade", "Second Grade", "Third Grade"], loc = 'lower right')


# Show the graph
plt.show()