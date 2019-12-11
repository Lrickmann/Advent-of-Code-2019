from day05.intcode import Intcode as Intc, Opcodes as Opc
import numpy as np

class Opcodes(Opc):

    def __init__(self):
        self.base = 0

    def reset_base(self):
        self.base = 0

    def get_values(self, array, pointer, codes, length, target):
        for i in range(length):
            if i == 0:
                continue
            elif i == target:
                codes[i] = array[pointer + i] + self.base if codes[i] == 2 else array[pointer + i]
            else:
                codes[i] = array[array[pointer + i] + self.base] if codes[i] == 2 else array[pointer + i] if codes[
                    i] == 1 else array[array[pointer + i]]
        return codes

    def opcode09(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=2)
        self.base += values[1]
        pointer += 2
        return arr, pointer, True


class Intcode(Intc):

    def load_input(self, input_name):
        self.array_orig = np.array(np.loadtxt(input_name, delimiter=",", dtype='int64'),dtype='object')

    def load_array(self, array):
        self.array_orig = np.array(array, dtype='object')

    def print_diagnostic_code(self):
        boolean = True
        pointer = 0
        array = self.get_array()
        while boolean:
            try:
                arr, pointer, boolean = self.compute(array, pointer)
            except IndexError:
                array = np.concatenate((array, np.zeros(len(array), dtype='object')))


if __name__ == '__main__':
    user_var = True
    op = Opcodes()
    op_codes = {'01': op.opcode01,
                '02': op.opcode02,
                '03': op.opcode03,
                '04': op.opcode04,
                '05': op.opcode05,
                '06': op.opcode06,
                '07': op.opcode07,
                '08': op.opcode08,
                '09': op.opcode09,
                '99': op.opcode99}
    print('test1:')
    arr1 = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    test = Intcode(function_dict=op_codes, user_input=1)
    test.load_array(arr1)
    test.print_diagnostic_code()
    print('test2:')
    arr2 = [1102,34915192,34915192,7,4,7,99,0]
    test = Intcode(function_dict=op_codes, user_input=1)
    test.load_array(arr2)
    test.print_diagnostic_code()
    print('test3:')
    arr3 = [104,1125899906842624,99]
    test = Intcode(function_dict=op_codes, user_input=1)
    test.load_array(arr3)
    test.print_diagnostic_code()
    while user_var:
        print("please give an input: ")
        user_var = int(input())
        op.reset_base()
        test = Intcode(function_dict=op_codes, user_input=user_var)
        test.load_input('../inputs/input09')
        test.print_diagnostic_code()
