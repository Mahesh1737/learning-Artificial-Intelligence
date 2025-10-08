import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


data = {
    'Area' : [1000, 1500, 1800, 2400, 3000],
    'Bedrooms' : [2, 3, 3, 4, 5], 
    'Price' : [300000, 400000, 500000, 600000, 650000]
}

df = pd.DataFrame(data)
print("DataFrame:",df)


X = df[['Area', 'Bedrooms']]
Y = df['Price']


model = LinearRegression()
model.fit(X,Y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(X)

result = pd.DataFrame({'Actual': Y, 'Predicted': y_pred})
print(result)


#mse
mse = mean_squared_error(Y, y_pred)
r2 = r2_score(Y, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)


plt.scatter(Y, y_pred, color='blue')
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.grid(True)
plt.show()
