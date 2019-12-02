import numpy as np


def compute(arr, mode, first, second, target):
    if mode == 1:
        arr[target] = arr[first] + arr[second]
        return arr, True
    elif mode == 2:
        arr[target] = arr[first] * arr[second]
        return arr, True
    elif mode == 99:
        return arr, False
    else:
        raise Exception("falscher mode")


array = np.loadtxt('../inputs/input02', delimiter=",", dtype=int)
array[1] = 12
array[2] = 2

print(array)

boolean = True
i = 0

while boolean:
    array, boolean = compute(array, array[i], array[i+1], array[i+2], array[i+3])
    i += 4

print(array)
