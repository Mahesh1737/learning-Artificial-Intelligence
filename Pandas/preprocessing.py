import pandas as pd
import numpy as np

#Load and do the preproccessing of the insurance dataset
data = pd.read_csv('insurance.csv')
print(data.head())

#Check for null values
print(data.isnull().sum())

#Check for duplicates
print(data.duplicated().sum())
print(data.duplicated().sum())

#Check for outliers
print(data.describe())

#Check for categorical variables
print(data.dtypes)

#Encoding categorical variables
data = pd.get_dummies(data, drop_first=True)

#Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

#Convert scaled data back to dataframe
data = pd.DataFrame(scaled_data, columns=data.columns)
print(data.head())

#Save the preprocessed data
data.to_csv('preprocessed_insurance.csv', index=False)

