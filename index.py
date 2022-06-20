import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import regression as reg
import random

df = pd.read_csv("./mushrooms.csv")

values = df.values

t = np.vectorize(ord)

values = t(values)

rows, columns = df.shape
for i in range(columns):
    values[:, i] = pd.factorize(values[:, i])[:][0]

rangesample = 1000

xColumn = values[:rangesample, 1:].T
yColumn = values[:rangesample, 0]

# Creating test data
# testweightcount = 2
# for i in range(testweightcount):
#     xColumn.append([])

# for i in range(rangesample):
#     val = .5
#     for j in range(testweightcount):
#         xColumn[j].append(random.random())
#         val += xColumn[j][i] * j
#     yColumn.append(val)
# xColumn = np.array(xColumn)
    


b, weights = reg.regression(.005, 1000, yColumn, xColumn)

plt.figure()

# [[ Weight display]]
# for i in range(len(weights)):
#     x1 = [0, b]
#     x2 = 1
#     y2 = weights[i]
#     plt.plot([0, 1], [b, weights[i]], marker="o")

def clamp(val, minv, maxv):
    return min(max(minv, val), maxv)

calculatedvals = []
actualvals = []
for i in range(25):
    actualvals.append(yColumn[i])
    calculatedvals.append(clamp(reg.predict(b, weights, xColumn[:, i]), 0, 1))
plt.plot(calculatedvals)
plt.plot(actualvals)
plt.show()
