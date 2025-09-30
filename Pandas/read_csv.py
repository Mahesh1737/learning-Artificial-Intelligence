# Basic CSV reading
df = pd.read_csv('Walmart_Sales.csv')
# with specific parameters
df = pd.read_csv('Walmart_Sales.csv',
sep=',',
# separator
header=0,
#row to use as column names
index_col=0,
# column to use as row Labels
na_values=['N/A', 'NULL'], # additional strings to recognize as NA
skiprows=1,
# skip first row
nrows=1000)
# read only first 1000 rows
# Reading with encoding
df pd.read_csv('Walmart_Sales.csv', encoding='utf-8') df