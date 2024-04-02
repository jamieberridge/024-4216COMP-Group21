import pandas as pd
import matplotlib.pyplot as plt

por = pd.read_csv("por2.csv")
maths = pd.read_csv("mat2.csv")

gradesByGender = por.groupby("sex",)["G3"].mean()
ax = gradesByGender.plot(kind="bar", xlabel="Gender", ylabel="Average Grade", title="Average Grade by Gender")
ax.set_xticklabels(["Male", "Female"])
ax.grid(True)

for i, grade in enumerate(gradesByGender):
    ax.text(i, grade + 0.1, f'{grade:.2f}', ha='center', va='bottom')


plt.xticks(rotation=0)
plt.show()