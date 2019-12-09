import numpy as np


def check_code(code):
    string = f"{code:05}"
    opcode = string[-2:]
    first = string[-3]
    second = string[-4]
    third = string[-5]
    return opcode, int(first), int(second), int(third)


def compute(arr, mode, pointer, base=0, input=1):
    opcode, first, second, third = check_code(mode)

    if opcode == '99':
        pointer += 1
        return arr, pointer, base, False

    first_val = arr[pointer + 1] if first == 1 else arr[arr[pointer + 1]] if first == 0 else arr[
        arr[pointer + 1] + base]
    if opcode != '03' and opcode != '04' and opcode != '09':
        second_val = arr[pointer + 2] if second == 1 else arr[arr[pointer + 2]] if second == 0 else arr[
            arr[pointer + 2] + base]
        if opcode != '05' and opcode != '06':
            third_val = arr[arr[pointer + 3] + base] if third == 2 else arr[
                pointer + 3]  # else arr[arr[pointer + 3]] if first == 0

    if opcode == '01':
        arr[third_val] = first_val + second_val
        pointer += 4
        return arr, pointer, base, True
    elif opcode == '02':
        arr[third_val] = first_val * second_val
        pointer += 4
        return arr, pointer, base, True
    elif opcode == '03':
        pointer += 2
        arr[arr[pointer + 1]] = input
        return arr, pointer, base, True
    elif opcode == '04':
        pointer += 2
        print(first_val)
        return arr, pointer, base, True
    elif opcode == '05':
        if not first_val:
            pointer += 3
        else:
            pointer = second_val
        return arr, pointer, base, True
    elif opcode == '06':
        if not first_val:
            pointer = second_val
        else:
            pointer += 3
        return arr, pointer, base, True
    elif opcode == '07':
        if first_val < second_val:
            arr[third_val] = 1
        else:
            arr[third_val] = 0
        pointer += 4
        return arr, pointer, base, True
    elif opcode == '08':
        if first_val == second_val:
            arr[third_val] = 1
        else:
            arr[third_val] = 0
        pointer += 4
        return arr, pointer, base, True
    elif opcode == '09':
        base += first_val
        pointer += 2
        return arr, pointer, base, True
    else:
        print(opcode)
        raise Exception("falscher mode")


array_orig = np.loadtxt('../inputs/input09', delimiter=",", dtype='int64')
# arr = np.array([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],dtype='object')
# arr = np.array([1102,34915192,34915192,7,4,7,99,0],dtype='object')
arr = np.array([104, 1125899906842624, 99], dtype='object')

boolean = True
pointer = 0
array = arr
rel_base = 0
while boolean:
    try:
        array, pointer, rel_base, boolean = compute(array, array[pointer], pointer, rel_base, input=5)
    except IndexError:
        array = np.concatenate((array, np.zeros(len(array), dtype='object')))

print("start real data")

boolean = True
pointer = 0
array = np.array(array_orig, dtype='object')
rel_base = 0
while boolean:
    try:
        array_t, pointer_t, rel_base_t, boolean_t = array, pointer, rel_base, boolean
        array, pointer, rel_base, boolean = compute(array, array[pointer], pointer, rel_base, input=1)
    except IndexError:
        array, pointer, rel_base, boolean = array_t, pointer_t, rel_base_t, boolean_t
        array = np.concatenate((array, np.zeros(len(array))))
