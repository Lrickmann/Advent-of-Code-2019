import pandas as pd

df = pd.read_csv("input1",header=None)

df = (df//3)-2

print(df.sum())
