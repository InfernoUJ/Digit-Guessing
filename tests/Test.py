import numpy as np
import unittest
import NeuralNetwork


class TestForwardPropagation(unittest.TestCase):
    def test_forward_propagation(self):
        nn = NeuralNetwork.NeuralNetwork(input_size=2, output_size=1, hidden_layers_number=1, hidden_layer_size=2, epsilon=.1)
        input_weights = np.array([[0.15, 0.2], [0.25, 0.3]])
        input_data = np.array([0.05, 0.1])
        expected_output = np.array([0.0325, 0.4])
        print(np.dot(input_data, input_weights))
        output = nn.forward_propagation(input_data, input_weights)
        print(output, expected_output)
        assert np.array_equal(output, expected_output)


if __name__ == "__main__":
    unittest.main()

