import numpy as np

def real_relu(x):
    return np.maximum(0, x)

def TEST_RELU(relu):
    inputs = np.arange(-8.0, 8.0, 0.1)

    y = real_relu(inputs)
    y_hat = relu(inputs)

    correct = np.sum(y == y_hat)
    total = len(inputs)

    print(f"Test Reuslt:")
    print(f"inputs: {total}")
    print(f"correct num : {correct}")
    print(f"acc : {(correct/total)*100:.2f}%")