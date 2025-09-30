import pandas as pd

#Sample DataFrame with text data
df = pd.DataFrame({
'names': [' Alice Johnson', 'bob smith', 'CHARLIE BROWN', 'diana_prince'],
'emails': ['alice@email.com', 'BOB@EMAIL.COM', 'charlie@email.com', 'diana@email.com'],
'phone': ['123-456-7890', '(123) 456-7890', '123.456.7890', '1234567890']
})

print("Original DataFrame:\n", df)


#Basic string operations
df['names_clean'] = df['names'].str.strip()# remove whitespace

print("Cleaned Names:\n", df['names_clean'])

df['names_upper'] = df['names'].str.upper()# convert to uppercase

print("Uppercase Names:\n", df['names_upper'])


df['names_lower'] = df['names'].str.lower()# convert to lowercase
print("Lowercase Names:\n", df['names_lower'])

# title case
df['names_title'] = df['names'].str.title()
print("Title Case Names:\n", df['names_title'])

# String length
df['name_length'] = df['names'].str.len()
print("Name Lengths:\n", df['name_length'])

# Replace strings
df['names_replaced'] = df['names'].str.replace('_','')
print("Replaced Names:\n", df['names_replaced'])

# Split strings
df['first_name'] = df['names_clean'].str.split().str[0]
print("First Names:\n", df['first_name'])

df['last_name'] = df['names_clean'].str.split().str[1]
print("Last Names:\n", df['last_name'])