import itertools
from PIL import Image
from os import getcwd, path
import numpy as np
from Data_Loader import DataLoader as Dl
import datetime


def improve(data):
    y = len(data)
    for j in range(y):
        minval, maxval = min(data[j]), max(data[j])
        tolerance = int(minval + (maxval - minval) / 1.43)
        x = len(data[j])
        for i in range(x):
            if data[j][i] <= tolerance:
                data[j][i] = 0
            else:
                data[j][i] = 255


def get_image(matrix, x, y):
    minval, maxval = min(matrix), max(matrix)
    tolerance = int(minval + (maxval - minval) / 1.43)
    _image_ = np.zeros((x, y))
    for i, j in itertools.product(range(x), range(y)):
        ix = (100 * i) + j
        if matrix[ix] <= tolerance:
            _image_[i][j] = 0
        else:
            _image_[i][j] = 255
    return Image.fromarray(_image_)


# initialise paths and lists
st = datetime.datetime.now()

parent_path = path.join(getcwd(), 'data', 'EmotionData')
directory_list = ['Angry', 'Confused', 'Happy', 'Neutral', 'Sad', 'Surprised']

# make dataset in form of a 1D array
data_loader = Dl(10, 6, parent_path, directory_list, 100, 100)
data_set = data_loader.make_data_set(directory_list)

"""
# perceptron training using masks as weight vector
improve(data_set)
image_training = Td.PTrainData(directory_list, 10)
image_training.train(data_set)

# Below code displays mask values.
img = get_image(image_training.get_mask('Surprised'), 100, 100)
plt.imshow(img)
et = datetime.datetime.now()
print(et - st)
plt.show()
"""
