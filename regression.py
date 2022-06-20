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

    lerror = 1
    itt = 0
    while lerror > .003:
        terr = 0
        itt += 1

        htable = []
        for i in nRange:
            htable.append(h(i))
        htable = np.array(htable)

        # weights
        for j in weightRange:
            err = np.sum((htable-yColumn)*xColumns[j])
            # for i in nRange:
            #     err += (htable[i]-yColumn[i])*xColumns[j][i]
            weights[j] -= learningRate*(err/n)
            terr += err

        # bias
        err = np.sum(htable-yColumn)
        b -= learningRate*(err/n)
        terr += err

        terr /= n*weightCount
        lerror = terr
        print("Average Err: ", terr, "Itteration: ", itt)

    return b, weights

def predict(bias, weights, values):
    val = bias
    for i in range(len(values)):
        val += values[i]*weights[i]
    return val