import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],  
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]    
})

print(df)

df_renamed = df.rename(columns={'A': 'Alpha', 'B': 'Beta'})
print("\nRenamed DataFrame:\n", df_renamed)

df_lower = df.rename(columns=str.lower)
print("\nColumns to Lowercase:\n", df_lower)

df_indexed_rename = df.rename(index={0: 'first', 1: 'second', 2: 'third', 3: 'fourth'})
print("\nRenamed Index:\n", df_indexed_rename)

df_dropped_col = df.drop(columns=['B'])
print("\nDataFrame after dropping column B:\n", df_dropped_col)


print("\nOriginal DataFrame remains unchanged:\n", df)

df_dropped_row = df.drop(index=[1, 3])
print("\nDataFrame after dropping rows with index 1 and 3:\n", df_dropped_row)

