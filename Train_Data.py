import numpy as np


class TrainData:
    def __init__(self, dir_list, imgs_in_dir):
        self.imgs_in_dir = imgs_in_dir
        self.dir_list = dir_list

    def train(self, data):
        raise NotImplementedError()


class PTrainData(TrainData):
    def __init__(self, dir_list, imgs_in_dir):
        super().__init__(dir_list, imgs_in_dir)
        self.mask_dict = {}
        for i in dir_list:
            self.mask_dict[i] = []

    def create_masks(self, data):
        x = len(data[0])
        _iter = 0
        for i in self.dir_list:
            mask_list = []
            for j in range(x):
                sumpixel = 0
                for k in range(self.imgs_in_dir):
                    sumpixel += data[_iter + k][j]
                sumpixel /= self.imgs_in_dir
                if sumpixel >= 225:
                    sumpixel = 255
                else:
                    sumpixel = 0
                mask_list.append(sumpixel)
            _iter += 10
            self.mask_dict[i] = mask_list

    def train(self, data):
        self.create_masks(data)
        # adjust weights, train perceptron

    def get_mask(self, expression):
        return self.mask_dict[expression]


class KNNTrainData(TrainData):
    def __init__(self, dir_list, imgs_in_dir, x, y):
        # data plotted in array plot_data
        super().__init__(dir_list, imgs_in_dir)
        self.x, self.y = x, y
        arr_size = len(dir_list) * imgs_in_dir
        self.plot_data = {}
        for i in dir_list:
            self.plot_data[i] = np.empty([self.x, self.y])

    def train(self, data):
        raise NotImplementedError()
