import math
from abc import ABC, abstractmethod


class ActivationFunction(ABC):

    @classmethod
    @abstractmethod
    def activate(cls, x: float) -> float:
        pass


class Sigmoid(ActivationFunction):

    @classmethod
    def activate(cls, x: float) -> float:
        return 1/(1+math.e**(-x))


class Tanh(ActivationFunction):

    @classmethod
    def activate(cls, x: float) -> float:
        # TODO maybe np.tanh()
        return math.tanh(x)


class ReLu(ActivationFunction):

    @classmethod
    def activate(cls, x: float) -> float:
        # TODO maybe np.tanh()
        return max(0, x)


if __name__ == "__main__":
    print(Sigmoid.activate(0.5))
    print(Tanh.activate(0.5))
    print(ReLu.activate(-0.5))

