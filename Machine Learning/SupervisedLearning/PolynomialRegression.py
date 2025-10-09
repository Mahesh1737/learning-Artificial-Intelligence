import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style 
import seaborn as sns

style.use('ggplot')

import warnings
warnings.filterwarnings('ignore')

# %matplotlib inline

df = pd.read_csv("Machine Learning\position.csv")
print("DataFrame:",df)

print("Duplicate Rows:",df.duplicated().sum())

print("Missing Values:",df.isnull().sum())

print("DataFrame Info:")
print(df.info())


plt.figure(figsize=(12,6), dpi=200)#dot per inch
sns.scatterplot(x='Level', y='Salary', data=df, color='blue')
plt.show()