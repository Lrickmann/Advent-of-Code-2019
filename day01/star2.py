import pandas as pd

df = pd.read_csv("input1", header=None)
fuel = 0


def rechnefuel(gewicht):
    ret = (gewicht // 3) - 2
    if ret < 0:
        return 0
    return ret


for index, line in df.iterrows():
    temp_fuel = rechnefuel(line[0])
    fuel += temp_fuel
    while temp_fuel > 0:
        temp_fuel = rechnefuel(temp_fuel)
        fuel += temp_fuel


print(fuel)
