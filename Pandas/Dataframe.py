import pandas as pd

# Creating DataFrame from dictionary
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'Diana'], 'Age': [25, 30, 35, 28], 'City': ['New York', 'London', 'Tokyo', 'Paris'], 'Salary': [50000, 60000, 70000, 55000]
}
print("Plain Data : \n",data)
df = pd.DataFrame(data)
print("DataFrame : \n",df)


# Creating DataFrame with custom index
df_indexed = pd.DataFrame (data, index=['empl', 'emp2', 'emp3', 'emp4'])
print("DataFrame with Custom Index : \n",df_indexed)


# From list of dictionaries


data_list = [
{
    'Name': 'Alice','Age': 25, 'City':'New York'
},
{
    'Name':'Bob','Age':30,'City':'London'
}
]

df_from_list = pd.DataFrame(data_list)
print("DataFrame from List of Dictionaries : \n",df_from_list)