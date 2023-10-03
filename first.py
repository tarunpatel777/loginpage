import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('data.csv')

# Basic data analysis
summary_stats = data.describe()
correlation_matrix = data.corr()

# Create a scatter plot
sns.scatterplot(x='feature1', y='feature2', data=data)
plt.title('Scatter Plot')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
