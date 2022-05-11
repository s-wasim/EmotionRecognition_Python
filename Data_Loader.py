import numpy as np
from os import path


class DataLoader:
    def __init__(self, files_in_dir, total_dir, par_path, dir_list, width, height):
        self.files_in_dir = files_in_dir
        self.total_dir = total_dir
        self.path_names = []
        for dir_name in dir_list:
            self.path_names.append(path.join(par_path, dir_name))
        self.data = np.empty((files_in_dir * total_dir, height * width), int)
        self.width = width
        self.height = height

    def print_path_names(self):
        print(self.path_names)

    def readpgm(self, f_name, j):
        file = open(f_name)
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        str_read = file.read()
        k = 0
        for i in str_read.split():
            if i.isdigit():
                self.data[j][k] = i
                k += 1

    def make_data_set(self, dir_list):

        for i in range(self.total_dir):
            for j in range(self.files_in_dir):
                f_name = path.join(self.path_names[i], dir_list[i] + str(j + 1) + '.pgm')
                self.readpgm(f_name, (i * self.files_in_dir) + j)
        return self.data
