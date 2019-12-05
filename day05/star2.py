import numpy as np


def check_code(code):
    string = f"{code:05}"
    opcode = string[-2:]
    first = string[-3]
    second = string[-4]
    third = string[-5]
    return opcode, int(first), int(second), int(third)


def compute(arr, mode, pointer, input=1):
    opcode, first, second, third = check_code(mode)

    if opcode == '99':
        pointer += 1
        return arr, pointer, False

    first_val = arr[pointer + 1] if first else arr[arr[pointer + 1]]
    if opcode != '03' and opcode != '04':
        second_val = arr[pointer + 2] if second else arr[arr[pointer + 2]]
        if opcode != '05' and opcode != '06':
            third_val = arr[pointer + 3]  # if third else arr[arr[pointer + 3]]

    if opcode == '01':
        arr[third_val] = first_val + second_val
        pointer += 4
        return arr, pointer, True
    elif opcode == '02':
        arr[third_val] = first_val * second_val
        pointer += 4
        return arr, pointer, True
    elif opcode == '03':
        pointer += 2
        arr[arr[pointer + 1]] = input
        return arr, pointer, True
    elif opcode == '04':
        pointer += 2
        print(first_val)
        return arr, pointer, True
    elif opcode == '05':
        if not first_val:
            pointer += 3
        else:
            pointer = second_val
        return arr, pointer, True
    elif opcode == '06':
        if not first_val:
            pointer = second_val
        else:
            pointer += 3
        return arr, pointer, True
    elif opcode == '07':
        if first_val < second_val:
            arr[third_val] = 1
        else:
            arr[third_val] = 0
        pointer += 4
        return arr, pointer, True
    elif opcode == '08':
        if first_val == second_val:
            arr[third_val] = 1
        else:
            arr[third_val] = 0
        pointer += 4
        return arr, pointer, True
    else:
        print(opcode)
        raise Exception("falscher mode")


array_orig = np.loadtxt('../inputs/input05', delimiter=",", dtype=int)
arr = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
       1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
       999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

boolean = True
pointer = 0
array = arr
while boolean:
    array, pointer, boolean = compute(array, array[pointer], pointer, input=5)

boolean = True
pointer = 0
array = array_orig.copy()
while boolean:
    array, pointer, boolean = compute(array, array[pointer], pointer, input=5)
