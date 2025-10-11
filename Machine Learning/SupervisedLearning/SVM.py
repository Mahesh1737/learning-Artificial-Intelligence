from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import sklearn.datasets


# Load dataset (e.g., Iris)

iris = sklearn.datasets.load_iris()
X = iris.data[:, :2] # Only 2 features for visualization

y = iris.target
# Use only 2 classes for binary classification
X = X[y != 2]
y = y[y != 2]

# Split into train and test
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.3, random_state=42)

#create svm model with linear kernel

model = SVC(kernel='linear', C=1.0)

model.fit(X_train,y_train)

#predict and evaluate
y_pred = model.predict(X_test)
print("Confusion matrix : \n",confusion_matrix(y_test, y_pred))

print("Classification report : \n",classification_report(y_test, y_pred))


