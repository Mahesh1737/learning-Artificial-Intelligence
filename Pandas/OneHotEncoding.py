# Categorical Encoding One-Hot Encoding
import pandas as pd

# Sample data with categories
df = pd.DataFrame({
'color': ['red', 'blue', 'green', 'red', 'blue'], 'size': ['small', 'medium', 'large', 'medium', 'small'], 'price': [10, 15, 20, 12, 8]
})
# Using pandas get_dummies
df_encoded = pd.get_dummies (df, columns=['color', 'size'])
print(df_encoded)


# Using sklearn OneHotEncoder
from json import encoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
encoder = OneHotEncoder (sparse_output=False, drop='first') # drop first to avoid multicollinearity
categorical_features = df[['color', 'size']]
encoded_features = encoder.fit_transform(categorical_features)
print(encoded_features)
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['color', 'size']))
print(encoded_df)
