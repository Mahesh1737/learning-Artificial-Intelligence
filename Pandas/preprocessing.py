import pandas as pd
import numpy as np

#Load and do the preproccessing of the insurance dataset
data = pd.read_csv('Pandas/insurance.csv')
print(data.head())

# Check for null values
print("Null values:",data.isnull().sum())

#Check for duplicates
print("Duplicate rows:",data.duplicated().sum())

#Check for outliers
print("Outliers:",data.describe())

#Check for categorical variables
print("Categorical variables:\n",data.dtypes)

#Encoding categorical variables
data = pd.get_dummies(data, drop_first=True)    
print("Encoded categorical features:\n", data.head())    


# #Feature scaling
# from sklearn.preprocessing import OneHotEncoder
# encoder = OneHotEncoder (sparse_output=False, drop='first') # drop first to avoid multicollinearity
# data = encoder.fit_transform(data)

# print("Scaled features:\n", data[:5])

# #Save the preprocessed data
data.to_csv('Pandas/insurance_preprocessed.csv', index=False)
