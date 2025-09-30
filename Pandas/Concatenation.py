# Sample DataFrames
df1 pd.DataFrame({'A': [1, 2], 'B': [3,4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})
# Concatenate vertically (default)
concat_vertical pd.concat([df1, df2])
print(concat_vertical)
# Concatenate horizontally
concat_horizontal pd.concat([df1, df3], axis=1)
print(concat_horizontal)
# Ignore index
concat_ignore_index = pd.concat([df1, df2], ignore_index=True)
print(concat_ignore_index )
# Add keys to identify source
concat_with_keys = pd.concat([df1, df2], keys=['first', 'second'])
print(concat_with_keys)
# Different handling of missing columns
concat_outer pd.concat([df1, df3], sort=False) # outer join (default)
print(concat_outer)
concat_inner pd.concat([df1, df3], join='inner') # inner join
print(concat_inner)