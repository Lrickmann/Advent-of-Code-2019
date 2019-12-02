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
        print(mode)
        raise Exception("falscher mode")


array_orig = np.loadtxt('../inputs/input02', delimiter=",", dtype=int)

done = False
counter = 4

for noun in range(100):
    for verb in range(100):
        boolean = True
        i = 0
        array = array_orig.copy()
        array[1] = noun
        array[2] = verb
        while boolean:
            if array[i] == 99:
                i += 1
                boolean = False
            else:
                array, boolean = compute(array, array[i], array[i+1], array[i+2], array[i+3])
                i += counter
        if array[0] == 19690720:
            print(100 * noun + verb)
            done = True
            break
    if done:
        break

