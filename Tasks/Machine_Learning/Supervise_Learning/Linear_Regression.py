import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv("Tasks/Machine_Learning/Supervise_Learning/datasets/Salary_dataset.csv")
print("DataFrame:",df)
# Define features and target variable
#independent variable
X = df[['YearsExperience']]
#dependent variable
y = df['Salary']

#train the model
model = LinearRegression()
model.fit(X, y)

#check coefficients
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict([[5.5], [7.5]])
print("Predicted salaries for 5.5 and 7.5 years of experience:", y_pred)

#plot
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.show()