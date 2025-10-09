import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
# Sample data
data={
"Outlook": ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy'],
"Humidity": ['High', 'High','High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'],
"kind": ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Strong'],
"Play": ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

print(df)

#Encode categorical data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop("Play", axis=1)
y = df["Play"]

#Train model
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
clf.fit(X, y)

#visualize the tree
plt.figure(figsize=(10,7))
tree.plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree")
plt.show()