import parameters as par
import numpy as np


def costFunction(position, trainingX, trainingResults):
    wLayer01 = np.zeros((par.layerNum[1], par.layerNum[0]))
    wLayer02 = np.zeros((par.layerNum[2], par.layerNum[1]))
    wLayer03 = np.zeros((par.layerNum[3], par.layerNum[2]))
    b0 = np.zeros((par.layerNum[0], 1))
    b1 = np.zeros((par.layerNum[1], 1))
    b2 = np.zeros((par.layerNum[2], 1))
    a1 = np.zeros((par.layerNum[1], 1))
    a2 = np.zeros((par.layerNum[2], 1))
    a3 = np.zeros((par.layerNum[3], 1))

    iterator = 0
    for i in range(par.layerNum[1]):
        for j in range(par.layerNum[0]):
            wLayer01[i, j] = position[iterator]
            iterator += 1

    iterator -= 1

    for i in range(par.layerNum[2]):
        for j in range(par.layerNum[1]):
            wLayer02[i, j] = position[iterator]
            iterator += 1

    iterator -= 1

    for i in range(par.layerNum[3]):
        for j in range(par.layerNum[2]):
            wLayer01[i, j] = position[iterator]
            iterator += 1

    iterator -= 1

    for i in range(par.layerNum[0]):
        b0[i, 1] = position[iterator]
        iterator += 1

    iterator -= 1

    for i in range(par.layerNum[1]):
        b1[i, 1] = position[iterator]
        iterator += 1

    iterator -= 1

    for i in range(par.layerNum[2]):
        b2[i, 1] = position[iterator]
        iterator += 1
