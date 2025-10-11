import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("Tasks/Machine_Learning/Supervise_Learning/datasets/multiple_linear_regression_dataset.csv")
print("DataFrame:\n",df.head())

# Define features and target variable
#independent variable
X = df[['age', 'experience']]
#dependent variable
y = df['income']    
#train the model
model = LinearRegression()
model.fit(X, y)

#check coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(X)
result = pd.DataFrame({'Actual': y, 'Predicted': y_pred})
print(result)
#plot
plt.scatter(y, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.grid(True)
plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)