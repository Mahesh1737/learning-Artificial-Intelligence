import numpy as np

# step 1 : Activation functions

#Sigmoid activation : squashes input between 0 and 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#derivative of sigmoid : used in backpropogation
def sigmoid_derivative(x):
    return x * (1 - x)



#step 2: xOr input and output

#input combinations of XOR gate(2 features each)

inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

#expected XOR outputs
outputs = np.array([[0], [1], [1], [0]])

#Step 3: initialize weights and biases

#seed for reproducibility

np.random.seed(42)

#2 nurons in hidden layer : shape (2 inputs -> 2 hidden)
weights_input_hidden = np.random.rand(2,2)

#1 neuron in output layer: shape (2 hidden -> 1 output)
weights_hidden_output = np.random.rand(2,1)

#biases (1 for each hidden and output neuron)

bias_hidden = np.random.rand(1, 2)
bias_output = np.random.rand(1, 1)

#step 4 : training parameters

#number of interations
epochs = 1000

#how much we change weights during training
learning_rate = 0.1



#Step 5 : training loop

for epoch in range(epochs):
    #forward pass : input to hidden layer
    hidden_input = np.dot(inputs, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)
    
    #hidden layer to output
    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(final_input)
    
    #backpropogation
    
    #calculate error
    error = outputs - predicted_output
    
    #Derivative for output layer
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    
    #error for hidden layer
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)
    
    
    
    #upddate weights and biases
    
    #update weights (gradient descent)
    
    weights_hidden_output += hidden_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += inputs.T.dot(d_hidden_layer) * learning_rate
    
    
    
    #update biases
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate
    
    #print loss every 1000 epochs
    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch}, loss : {loss: .4f}")
        
# step 6 final prediction

print("\n Final predictions after training: ")
print(np.round(predicted_output, 2))
