import PIL
from PIL import Image
import os
import random


class ImageSupplier:
    __path_to_data_images = os.path.join("data")

    def __init__(self, data_set_size: int, percent_of_train_data: float):
        if not (0 < percent_of_train_data < 1):
            raise ValueError("percent_of_train_data must be between 0 and 1")
        self.percent_of_train_data = percent_of_train_data
        self.data_set_size = data_set_size

    def __prepare_labels(self):
        self.train_data = [[] for _ in range(10)]
        self.test_data = [[] for _ in range(10)]

        for digit in range(10):
            self.train_data[digit] = random.sample(range(1, 1001), k=self.data_set_size//10)
            self.test_data[digit] = random.sample(self.train_data[digit], k=int(self.data_set_size*(1-self.percent_of_train_data)/10))
            self.train_data[digit] = [x for x in self.train_data[0] if x not in self.test_data[0]]

    def __make_sequence(self, data, sequence):
        sequence.clear()
        for digit in range(10):
            for image_number in data[digit]:
                image = Image.open(os.path.join(self.__path_to_data_images, str(digit), str(digit) + '_' + str(image_number) + ".jpg"))
                image = image.resize((32, 32))
                image = image.convert('L')
                sequence.append((digit, image))
        random.shuffle(sequence)

    def __make_train_sequence(self):
        self.train_sequence = []
        self.__make_sequence(self.train_data, self.train_sequence)

    def __make_test_sequence(self):
        self.test_sequence = []
        self.__make_sequence(self.test_data, self.test_sequence)

    def prepare_dataset(self):
        self.__prepare_labels()
        # print(len(self.train_data[0]), len(set(self.train_data[0])), self.train_data[0])
        # print(len(self.test_data[0]), self.test_data[0])
        # print(len(set(self.train_data[0]).intersection(set(self.test_data[0]))))
        self.__make_train_sequence()
        # print(self.train_sequence)
        self.__make_test_sequence()

    def get_train_data(self):
        return iter(self.train_sequence)

    def get_test_data(self):
        return iter(self.test_sequence)


if __name__ == "__main__":
    im = ImageSupplier(1000, 0.8)
    im.prepare_dataset()
    data = im.get_train_data()










