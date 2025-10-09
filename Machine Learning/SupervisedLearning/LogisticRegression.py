import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline


df = pd.read_csv('Machine Learning\SupervisedLearning\position.csv')
print(df.head()) 

plt.scatter(df['Level'], df['Salary'], marker="+", color='red')
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['Level']], df['Salary'], test_size=0.2)

print("X testing data: \n",X_test)
print("X training data: \n",X_train)
print("y testing data: \n",y_test)
print("y training data: \n",y_train)