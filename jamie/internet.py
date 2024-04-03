import pandas as pd
import matplotlib.pyplot as plt

# Read Datasets and store them
por = pd.read_csv("por2.csv")
maths = pd.read_csv("mat2.csv")

# Group both datasets by internet then calculate the mean of each
mathsGradesByInternet = maths.groupby("internet",)["G3"].mean()
porGradesByInternet = por.groupby("internet",)["G3"].mean()

# Concatinate both groups in order to have a complete view
gradesByInternet = pd.concat([mathsGradesByInternet, porGradesByInternet], axis=0)

# Made the window the appropriate size to fit the bar charts
plt.figure(figsize=(10, 7))

# Create a bar chart for each group in gradesByInternet
plot = gradesByInternet.plot(kind="bar", xlabel="Internet Access", ylabel="Average Grade", title="Average Grade by Internet Access", width = 0.8)
plot.set_xticklabels(["Maths \nInternet Access", "Maths \nNo Internet Access", "Portuguese \nInternet Access", "Portuguese \nNo Internet Access"])
# Add a grid for better readability
plot.grid(True)

#  Set labels for the top of each bar to show their y value
for i, grade in enumerate(gradesByInternet):
    plot.text(i, grade + 0.1, f'{grade:.2f}', ha='center', va='bottom')

# Rotate the labels on the x axis
plt.xticks(rotation=0)
# Open and show the window
plt.show()