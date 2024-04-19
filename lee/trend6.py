
#Reason for going to higher education and higher education

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
por = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Group the data by reason for going to higher education
mathsHigherEdu = maths.groupby(by = 'higher')['reason']
porHigherEdu = por.groupby(by = 'higher')['reason']


# Setting size of the window
plt.figure(figsize=(15, 7))

# Plot for Maths
plt.subplot(1, 2, 1)
plt.pie(mathsHigherEdu.value_counts(), labels = mathsHigherEdu.value_counts().index, textprops={'size': 'smaller'}, autopct='%1.1f%%')
plt.title('Reason for going to higher education (Maths)')
plt.axis('equal')
# Plot for Portuguese
plt.subplot(1, 2, 2)
plt.pie(porHigherEdu.value_counts(), labels = porHigherEdu.value_counts().index, textprops={'size': 'smaller'}, autopct='%1.1f%%')
plt.title('Reason for going to higher education (Portuguese)')
plt.axis('equal')
plt.tight_layout()
plt.show()