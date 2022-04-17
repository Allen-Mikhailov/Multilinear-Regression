import pandas as pd
import numpy as np
df = pd.read_csv("./mushrooms.csv")

values = df.values

t = np.vectorize(ord)

values = t(values)

for i in range(1):
    vals = values[:, i]
    mn = vals.min()
    mx = vals.max()
    vals -= mn
    values[:, i] = vals / int(mx-mn)

print(values[:, 0])
print(df.values[:, 0])