from mlxtend.data import loadlocal_mnist
import platform
import numpy as np

if not platform.system() == 'Windows':                  # X is the training samples, y is the result of the training sample
    X, y = loadlocal_mnist(
            images_path='train-images-idx3-ubyte',
            labels_path='train-labels-idx1-ubyte')

else:
    X, y = loadlocal_mnist(
            images_path='train-images.idx3-ubyte',
            labels_path='train-labels.idx1-ubyte')




