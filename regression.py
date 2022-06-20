import random
import numpy as np

def regression(learningRate, itterations, yColumn, xColumns):
    weightCount = len(xColumns)
    weightRange = range(weightCount)

    yColumn = np.array(yColumn)
    xColumns = np.array(xColumns)
    xColumnsT = xColumns.T

    n = len(yColumn)
    nRange = range(n)

    b = random.random()

    weights = []
    for i in weightRange:
        weights.append(random.random())

    def h(row):
        return b + np.sum(weights*xColumnsT[row])

    for itt in range(itterations):
        terr = 0

        # weights
        for j in weightRange:
            err = 0
            for i in nRange:
                err += (h(i)-yColumn[i])*xColumns[j][i]
            weights[j] -= learningRate*(err/n)
            terr += err

        # bias
        err = 0
        for i in nRange:
            err += (h(i)-yColumn[i])
        b -= learningRate*(err/n)
        terr += err

        terr /= n*weightCount
        print("Average Err: ", terr)

    return b, weights

def npregression(learningRate, itterations, yCollum, xCollums):
    yCollum = np.array(yCollum)
    xCollums = np.array(xCollums)

    weightCount = len(xCollums)
    weightRange = range(weightCount)

    n = len(yCollum)
    nRange = range(n)

    b = random.random()

    weights = []
    for i in weightRange:
        weights.append(random.random())
    weights = np.array(weights)

    def h():
        return 


def predict(bias, weights, values):
    val = bias
    for i in range(len(values)):
        val += values[i]*weights[i]
    return val