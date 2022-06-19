import pandas as pd
import numpy as np
df = pd.read_csv("./mushrooms.csv")

values = df.values

t = np.vectorize(ord)

values = t(values)

rows, columns = df.shape
for i in range(columns):
    values[:, i] = pd.factorize(values[:, i])[:][0]

xColumn = values[:, ]