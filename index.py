import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import regression as reg
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


b, weights = reg.regression(.01, 1000, yColumn, xColumn)
print(b, weights)

plt.figure()

# for i in range(len(weights)):
#     x1 = [0, b]
#     x2 = 1
#     y2 = weights[i]
#     plt.plot([0, 1], [b, weights[i]], marker="o")
plt.show()
