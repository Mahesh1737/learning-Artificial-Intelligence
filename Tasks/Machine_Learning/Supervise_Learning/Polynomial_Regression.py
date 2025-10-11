import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures


style.use('ggplot')

import warnings
warnings.filterwarnings('ignore')

# %matplotlib inline

df = pd.read_csv("Tasks/Machine_Learning/Supervise_Learning/datasets/Ice_cream selling data.csv")
print("Dataset : \n",df.head())

print("Duplicate Rows:",df.duplicated().sum())

print("Missing Values:",df.isnull().sum())

print("DataFrame Info:")
print(df.info())


plt.figure(figsize=(12,6), dpi=200)#dot per inch
sns.scatterplot(x='Temperature (°C)', y='Ice Cream Sales (units)', data=df, color='blue')
plt.show()