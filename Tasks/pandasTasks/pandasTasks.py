import pandas as pd

#Creating the Series
temps = [22, 25, 28, 32, 35, 33, 30, 28, 26, 23, 20, 18]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

temp_series = pd.Series(temps, index=months)
print("Monthly Temperatures:\n", temp_series, "\n")

# printing Hottest and coldest months
print("Hottest Month:", temp_series.idxmax(), "with", temp_series.max(), "°C")
print("Coldest Month:", temp_series.idxmin(), "with", temp_series.min(), "°C\n")

# finding Average temperature
print("Average Temperature:", temp_series.mean(), "°C\n")

#Finding Months with temperature above 25°C
print("Months with temp > 25°C:\n", temp_series[temp_series > 25], "\n")

# Printing Temperature in Fahrenheit
temp_f = temp_series * 9/5 + 32
print("Temperatures in Fahrenheit:\n", temp_f)

# creating Employee data
df = pd.DataFrame({
    'emp_id': [101,102,103,104,105],
    'name': ['Alice Johnson','Bob Smith','Carol Williams','David Brown','Eve Davis'],
    'department': ['IT','HR','Finance','IT','Marketing'],
    'salary': [75000,60000,80000,70000,65000],
    'experience': [5,3,8,4,2]
})

# Set emp_id as a index
df.set_index('emp_id', inplace=True)

# Adding new columns
df['salary_per_experience'] = df['salary'] / df['experience']
df['high_earner'] = df['salary'] > 70000

# Display info, stats, and DataFrame
print(df.info())
print(df.describe())
print(df)

# Create sales DataFrame
df = pd.DataFrame({
    'date': pd.date_range('2025-01-01', periods=15),
    'product': ['Laptop','Phone','Tablet','Laptop','Phone','Tablet','Laptop','Phone','Tablet','Laptop', None,'Phone','Tablet', None,'Laptop'],
    'quantity': [5,10,3,8,15,7,6,9,4,11,2,12,5,8,10],
    'price': [800,500,300,850,520,310,810,490,320,870,305,515,295,825,805],
    'region': ['North','South','East','West','North','South','East','West','North','South','East', None,'West','North','South']
})

# Saving CSV file
df.to_csv('sales_data.csv', index=False)

# Reading CSV File with different options
print(pd.read_csv('sales_data.csv', skiprows=1).head())        # skip first row
print(pd.read_csv('sales_data.csv', nrows=10))                # first 10 rows
print(pd.read_csv('sales_data.csv', index_col='date').head()) # date as index
print(pd.read_csv('sales_data.csv').fillna('Unknown').head()) # handle missing values

# Saving only specific columns
df[['product','quantity','price']].to_csv('sales_subset.csv', index=False)

# Sample student data
df = pd.DataFrame({
    'student_id': range(1, 21),
    'math': [78, 65, 89, 92, 56, 81, 74, 95, 67, 88,
             45, 60, 83, 79, 91, 55, 72, 86, 69, 94],
    'science': [82, 74, 91, 68, 77, 85, 73, 90, 62, 87,
                58, 64, 80, 76, 95, 70, 66, 84, 72, 93],
    'english': [70, 68, 75, 80, 64, 78, 72, 85, 60, 77,
                55, 62, 79, 74, 88, 65, 71, 83, 69, 90],
    'grade': [10, 11, 12, 11, 10, 12, 11, 12, 10, 11,
              12, 10, 11, 12, 12, 10, 11, 12, 11, 12],
    'age': [16, 17, 18, 17, 16, 18, 17, 18, 16, 17,
            18, 16, 17, 18, 18, 16, 17, 18, 17, 18]
}).set_index('student_id')

# --- loc tasks ---
print("IDs 5,10,15:\n", df.loc[[5,10,15]])
print("\nMath & Science (1–10):\n", df.loc[1:10, ['math','science']])
print("\nMath > 80:\n", df.loc[df['math'] > 80])

# --- iloc tasks ---
print("\nFirst 5 students, first 3 cols:\n", df.iloc[:5, :3])
print("\nEvery 3rd student:\n", df.iloc[::3])
print("\nLast 3 students, last 2 cols:\n", df.iloc[-3:, -2:])

# --- Boolean indexing tasks ---
print("\nAbove 85 in all subjects:\n", df[(df['math']>85)&(df['science']>85)&(df['english']>85)])
print("\n12th graders with math < 70:\n", df[(df['grade']==12)&(df['math']<70)])
print("\nAge 17/18 with science > avg:\n", df[(df['age'].isin([17,18])) & (df['science']>df['science'].mean())])