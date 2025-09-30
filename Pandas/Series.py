import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
print(s)

b = pd.Series([10, 20, 30, 40, 50], ['a', 'b', 'c', 'd', 'e'])
print(b)

Dict = {'a': 100, 'b': 200, 'c': 300}
d = pd.Series(Dict)
print(d)