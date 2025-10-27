import numpy as np
import pandas as pd

# Step 1: Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Step 2: Load and preprocess dataset
df = pd.read_csv('Deep Learning/Datasets/Churn_Modelling.csv')

# Select features (CreditScore to EstimatedSalary) and target (Exited)
X = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values.reshape(-1, 1)

# Encode categorical variables (Geography, Gender)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

ct = ColumnTransformer([('encoder', OneHotEncoder(drop='first'), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Step 3: Initialize weights and biases
np.random.seed(42)
n_input = X.shape[1]   # 11 features after encoding
n_hidden = 6           # 6 neurons in hidden layer
n_output = 1           # 1 neuron for binary output

# Random initialization
weights_input_hidden = np.random.randn(n_input, n_hidden)
weights_hidden_output = np.random.randn(n_hidden, n_output)
bias_hidden = np.random.randn(1, n_hidden)
bias_output = np.random.randn(1, n_output)

# Step 4: Training parameters
epochs = 500
learning_rate = 0.05

# Step 5: Training loop
for epoch in range(epochs):
    # Forward pass
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(final_input)

    # Error
    error = y - predicted_output

    # Backpropagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights and biases
    weights_hidden_output += hidden_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Print loss occasionally
    if epoch % 50 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Step 6: Final results
print("\nTraining complete.")
print("Sample Predictions (first 10):")
print(np.round(predicted_output[:10], 2))
print("Actual:", y[:10].ravel())
