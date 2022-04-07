import random


def regression(learningRate, itterations, yCollum, xCollums):
    weightCount = len(xCollums)
    weightRange = range(weightCount)

    n = len(yCollum)
    nRange = range(n)

    b = random.random()

    weights = []
    for i in weightRange:
        weights.append(random.random())

    def h(row):
        v = b
        for j in weightRange:
            v += weights[j] * xCollums[j][row]

        return v

    for itt in range(itterations):
        # weights
        for j in weightRange:
            err = 0
            for i in nRange:
                err += (h(i)-yCollum[i])*xCollums[j][i]
            weights[j] -= learningRate*(err/n)

        # bias
        err = 0
        for i in nRange:
            err += (h(i)-yCollum[i])
        b -= learningRate*(err/n)

        return b, weights
