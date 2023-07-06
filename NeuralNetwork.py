import ActivationFunction
import numpy as np


class NeuralNetwork:

    def __init__(self, input_size: int, output_size: int, hidden_layers_number: int, hidden_layer_size: int, epsilon: float,
                 activation_function: ActivationFunction = ActivationFunction.Sigmoid):
        self.__input_size = input_size
        self.__output_size = output_size
        self.__hidden_layers_number = hidden_layers_number
        self.__hidden_layer_size = hidden_layer_size
        self.__epsilon = epsilon
        self.__activation_function = activation_function
        self.__activation_vectorize = np.vectorize(self.__activation_function.activate)

        # Creating weights
        self.inputWeights = np.random.rand(self.__hidden_layer_size, self.__input_size)
        self.outputWeights = np.random.rand(self.__hidden_layer_size, self.__output_size)
        self.middleWeights = np.array([np.random.rand(self.__hidden_layer_size, self.__hidden_layer_size) for i in range(self.__hidden_layers_number - 1)])

    def __forward_propagation(self, input_data: np.ndarray, weights: np.ndarray) -> np.ndarray:
        output = np.dot(input_data, weights)
        return self.__activate(output)

    def __activate(self, data_to_activate: np.ndarray) -> np.ndarray:
        return self.__activation_vectorize(data_to_activate)








    




















