import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': ['apple', 'banana', 'cherry', 'date']

})

def square(x):
    return x ** 2 if isinstance(x, (int, float)) else x

df_squared = df.apply(square)
print("DataFrame with Squared Values using apply:\n", df_squared)

df['A_squared'] = df['A'].apply(lambda x: x ** 2)
print("DataFrame with Squared Values:\n", df['A_squared'])

#applying multiple columns
df['A_plus_B'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print("DataFrame with A + B:\n", df['A_plus_B'])




# Apply function to entire DataFrame
def square(x):
    return x ** 2 if isinstance(x, (int, float)) else x
df_squared = df.apply(square)


#Apply to specific column
df['A_squared'] = df ['A'].apply(lambda x: x ** 2)
print(df['A_squared'])


# Apply to multiple columns
df[['A', 'B']] = df[['A', 'B']].apply(lambda x: x * 2)
print(df[['A', 'B']])


#Apply row-wise (axis=1)
df ['A_plus_B'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df['A_plus_B'])


# Using map (only for Series)
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
df ['A_mapped'] = df['A'].map(mapping)
print(df['A_mapped'])


#Apply with additional arguments
def multiply_by_n(x, n):
    return x *n

df['A_times_3'] = df['A'].apply(multiply_by_n, n=3)
print(df['A_times_3'])