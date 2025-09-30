# Basic JSON reading
df = pd.read_json('data.json')
# Different orientations
df = pd.read_json('data.json', orient='records')
# list of records
df = pd.read_json('data.json', orient='index')
# index-oriented
df = pd.read_json('data.json', orient='values')
# values-oriented
# From JSON string
json_string = '{"Name": ["Alice", "Bob"], "Age": [25, 30]}'
df = pd.read_json(json_string)