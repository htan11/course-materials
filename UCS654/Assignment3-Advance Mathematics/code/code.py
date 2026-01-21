#Harsh Tanwar 102303812

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv", encoding="latin1")
x = df["no2"].dropna().values

r = 102303812
ar = 0.05 * (r % 7)
br = 0.3 * ((r % 5) + 1)

z = x + ar * np.arcsin(np.clip(br * x, -1, 1))

mu = z.mean()
var = z.var()
lam = 1 / (2 * var)
c = np.sqrt(lam / np.pi)

mu, lam, c
