# Importing Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Read the csv files
df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')

# Assigning the columns to variables
x1 = df_2018['Score'].quantile(np.linspace(0,1,156))
x2 = df_2019['Score'].quantile(np.linspace(0,1,156))

# Plotting the Q-Q plot
plt.figure(figsize=(8, 6))
plt.scatter(x1,x2)
plt.plot([min(x1),max(x1)],[min(x1),max(x1)],color="red")
plt.xlabel("Score for 2018")
plt.ylabel("Score for 2019")
plt.title('Q-Q Plot for World Happiness Scores (2017 vs. 2018)')
plt.legend()
plt.grid(True)
plt.show()