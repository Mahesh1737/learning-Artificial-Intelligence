# Feature Engineering Creating New Features
# Sample dataset

import pandas as pd
import numpy as np

df = pd.DataFrame({
'date': pd.date_range('2023-01-01', periods=100),
'sales': np.random.randint(100, 1000, 100),
'temperature': np.random.normal(25, 10, 100),
'price': np.random.uniform (10, 100, 100),
'quantity': np.random.randint(1, 20, 100)
})


# Date-based features
df['year'] = df ['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6])
df['quarter'] = df ['date'].dt.quarter
print(df[['date', 'year', 'month', 'day_of_week', 'is_weekend', 'quarter']].head())


# Mathematical operations
df['revenue'] = df['price'] * df['quantity']
df['price_per_unit'] = df['sales'] / df['quantity']
df['log_sales'] = np.log(df ['sales'])


# Binning continuous variables
df['temp_category'] = pd.cut(df['temperature'],
bins=[-np.inf, 10, 20, 30, np.inf], labels=['Cold', 'Cool', 'Warm', 'Hot'])

# Rolling statistics
df['sales_7day_avg'] = df['sales'].rolling (window=7).mean()
df['sales_7day_std'] = df['sales'].rolling(window=7).std()

# Lag features
df['sales_lag1'] = df['sales'].shift(1)
df['sales_lag7'] = df['sales'].shift(7)
print(df.head(10))