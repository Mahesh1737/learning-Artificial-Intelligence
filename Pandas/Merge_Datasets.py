import pandas as pd

#Sample DataFrames
df1 = pd.DataFrame({
'id': [1, 2, 3, 4],
'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
'age': [25, 30, 35, 28]
})

df2 = pd.DataFrame({
'id': [1, 2, 3, 5],
'department': ['IT', 'HR', 'Finance', 'Marketing'],
'salary': [50000, 60000, 70000, 55000]
})


print("DataFrame 1:\n", df1)
print("DataFrame 2:\n", df2)

# Inner merge (default)
merged_inner = pd.merge(df1, df2, on='id')
print("Merged Inner:\n", merged_inner)

#Left merge
merged_left = pd.merge(df1, df2, on='id', how='left')
print("Merged Left:\n",merged_left)

# Right merge
merged_right = pd.merge(df1, df2, on='id', how='right')
print("Merged Right:\n", merged_right)

#Outer merge
merged_outer = pd.merge(df1, df2, on='id', how='outer')
print("Merged Outer:\n", merged_outer)

#Merge on different column names
df3 = pd.DataFrame({
'employee_id': [1, 2, 3],
'project': ['A', 'B', 'C']
})

print("DataFrame 3:\n", df3)

merged_diff_col = pd.merge(df1, df3, left_on='id', right_on='employee_id')
print("Merged on Different Column Names:\n", merged_diff_col)


merged_diff_cols = pd.merge(df1, df3, left_on='id', right_on='employee_id')
print(merged_diff_cols)
#Merge on multiple columns
df4 = pd.DataFrame({
'id': [1, 1, 2, 2],
'year': [2022, 2023, 2022, 2023],
'performance': ['Good', 'Excellent', 'Fair', 'Good']
})

dfs  = pd.DataFrame({
'id': [1, 1, 2, 2],
'year': [2022, 2023, 2022, 2023],
'bonus': [1000, 1500, 500, 800]
})
merged_multi  = pd.merge(df4, df5, on=['id', 'year'])
print(merged_multi)