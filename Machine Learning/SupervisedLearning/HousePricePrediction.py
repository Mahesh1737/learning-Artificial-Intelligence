import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'Area' : [1000, 1500, 1200, 1800, 2000],
    'Bedrooms' : [2, 3, 2, 4, 4],
    'Age' : [5, 7, 3, 10, 2],
    'Price' : [50, 65, 55, 70, 85]
}

df = pd.DataFrame(data)
print("DataFrame:",df)

# Define features and target variable
#independent variable
X = df[['Area']]
#dependent variable
y = df['Price']

#train the model
model = LinearRegression()
model.fit(X, y)

#check coefficients
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict([[1600]])
print("Predicted prices for 1600 and 2000 sq ft areas:", y_pred)


#plot

plt.figure(figsize=(8,5))

plt.bar(range(len(y)), y, label='Actual Price' , color='b', alpha=0.6)
plt.bar(range(len(y_pred)), y_pred, label='Predicted Price', color='r', alpha=0.6)
plt.xlabel('House Index')
plt.ylabel('Price in lakhs')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.grid(True)
plt.show()


#Evaluate the train model

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
y_pred = model.predict(X)
# mean_absolute_error_value = mean_absolute_error(y, y_pred)

#mse tells how far your model's predictions are from the actual values
mean_squared_error_value = mean_squared_error(y, y_pred)

#R^2 score tells how well the model explains the variability of the target variable
r2_score_value = r2_score(y, y_pred)

print("Mean Squared Error:", mean_squared_error_value)
print("R^2 Score:", r2_score_value)


#Residual plot
#residual checks for the error, if points are randomly distributed around horizontal axis, it means linear regression model is good fit for the data
#around zero the model is good fit
residuals = y - y_pred

plt.figure(figsize=(8,5))
plt.scatter(y_pred, residuals, color='blue', alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Prices')
plt.ylabel('Residuals error')
plt.title('Residual Plot')
plt.grid(True)
plt.show()