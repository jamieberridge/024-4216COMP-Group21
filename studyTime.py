# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the datasets into pandas DataFrames
portuguese = pd.read_csv('por2.csv')
maths = pd.read_csv('mat2.csv')

# Extract relevant columns
travel_time = maths['traveltime']
study_time = maths['studytime']

# Add jitter to the data for better visualization
jitter = 0.2  # Adjust the jitter magnitude as needed
travel_time_jitter = travel_time + np.random.uniform(-jitter, jitter, len(travel_time))
study_time_jitter = study_time + np.random.uniform(-jitter, jitter, len(study_time))

# Plot the scatter plot with jitter
plt.figure(figsize=(8, 6))
plt.scatter(travel_time_jitter, study_time_jitter, color='blue', alpha=0.5)

# Add labels and title
plt.xlabel('Travel Time')
plt.ylabel('Study Time')
plt.title('Scatter Plot of Travel Time vs. Study Time')

# Add grid
plt.grid(True)

plt.tight_layout()
plt.show()
