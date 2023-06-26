import numpy as np

def perceptron_trick(X, y, learning_rate=0.1, max_iterations=100):
    num_features = X.shape[1]
    num_samples = X.shape[0]

    # Initialize weights and bias
    weights = np.zeros(num_features)
    bias = 0

    for _ in range(max_iterations):
        total_error = 0

        for i in range(num_samples):
            # Compute predicted class label
            prediction = np.sign(np.dot(weights, X[i]) + bias)
            if prediction != y[i]:
                weights += learning_rate * y[i] * X[i]
                bias += learning_rate * y[i]
                total_error += 1
        if total_error == 0:
            break

    return weights, bias


X = np.array([[1, 2], [2, 3], [3, 1], [4, 3]])
y = np.array([1, 1, -1, -1])

weights, bias = perceptron_trick(X, y)
print("Learned weights:", weights)
print("Learned bias:", bias)
