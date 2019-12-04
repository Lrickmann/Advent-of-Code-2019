import pandas as pd

df = pd.read_csv("../inputs/input01",header=None)
df = (df//3)-2
print(df.sum())
