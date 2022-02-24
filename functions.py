import numpy as np


def linearActivation(x):
    return np.maximum(0.0, x)


def relu(matrice):
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):
            matrice[i, j] = linearActivation(matrice[i, j])
    return matrice


# def activationCalculator(weight,lastActivation,bias):
#     a = 10
#     return a


# m = np.ones(5)
# k = relu(m)
# print(m.shape)
# print(k)
print(8 / 5 * (1) + 3 ** .7)
