import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns


# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
#print(url)
data = pd.read_csv(url)
data.head()


# Drop irrelevant columns
data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Fill missing values
data['Age'].fillna (data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode() [0], inplace=True)

# Encode categorical variables
le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])

#Male=1, Female=0
data['Embarked'] = le.fit_transform(data['Embarked'])

# Features and target
X = data.drop('Survived', axis=1)
y = data['Survived']
print(y)


#split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Create a Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

#Train the model
rf.fit(X_train, y_train)

#make predictions
y_pred = rf.predict(X_test)

#Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

#Visualize feature importance
feature_importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=feature_importances, y=feature_importances.index)
plt.title("Feature Importances")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.show()