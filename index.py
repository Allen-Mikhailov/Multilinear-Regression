import pandas as pd
import numpy as np
df = pd.read_csv("./mushrooms.csv")

values = df.values

t = np.vectorize(ord)

values = t(values)
values = values.astype(float)

rows, collums = df.shape
for i in range(collums):
    vals = values[:, i]
    mn = vals.min()
    mx = vals.max()
    vals -= mn
    values[:, i] = vals / (mx-mn)

    print(values[:, i])
    print(df.values[:, i])