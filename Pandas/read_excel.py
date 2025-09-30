# Basic Excel reading
df = pd.read_excel('data.xlsx')
# Specific sheet
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
# Multiple sheets
dfs = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'Sheet2'])
# With parameters
df = pd.read_excel('data.xlsx',
sheet_name=0,
# first sheet
header=1,
# second row as header
skiprows=2)
# skip first 2 rows