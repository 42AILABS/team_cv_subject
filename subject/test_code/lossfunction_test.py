import numpy as np
from numpy.testing import assert_almost_equal

def generate_random_probabilities(batch_size, num_classes):
    raw_probabilities = np.random.random((batch_size, num_classes))
    return raw_probabilities / raw_probabilities.sum(axis=1, keepdims=True)

def reference_cross_entropy(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]

def TEST_CROSS_ENTROPY(cross_entropy):
    np.random.seed(42)
    
    test_configs = [
        (32, 2),    # binary classification, batch size 32
        (64, 3),    # 3 classes, batch size 64
        (128, 5),   # 5 classes, batch size 128
        (256, 10),  # 10 classes, batch size 256
    ]
    
    total_tests = len(test_configs) + 1  # +1 for perfect prediction case
    passed_tests = 0
    
    for batch_size, num_classes in test_configs:
        try:
            # Generate predictions
            y_pred = generate_random_probabilities(batch_size, num_classes)
            
            # Generate true values
            y_true = np.zeros((batch_size, num_classes))
            true_classes = np.random.randint(0, num_classes, size=batch_size)
            y_true[np.arange(batch_size), true_classes] = 1
            
            # Compare results
            expected = reference_cross_entropy(y_true, y_pred)
            result = cross_entropy(y_true, y_pred)
            
            # Validate results
            relative_error = np.abs(result - expected) / (np.abs(expected) + 1e-15)
            assert relative_error < 1e-5
            
            passed_tests += 1
            
        except Exception:
            continue
    
    # Test perfect prediction case
    try:
        y_true = np.array([[1, 0], [0, 1]])
        y_pred = np.array([[1.0, 0.0], [0.0, 1.0]])
        result = cross_entropy(y_true, y_pred)
        assert_almost_equal(result, 0.0, decimal=5)
        passed_tests += 1
    except Exception:
        pass

    print(f"TEST result {passed_tests} / {total_tests} Pass")