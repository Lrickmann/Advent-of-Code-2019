import numpy as np


class Opcodes(object):

    def __init__(self):
        pass

    def get_values(self, array, pointer, codes, length, target):
        for i in range(length):
            if i == 0:
                continue
            elif i == target:
                codes[i] = array[pointer + i]
            else:
                codes[i] = array[pointer + i] if codes[i] else array[array[pointer + i]]
        return codes

    def opcode01(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=4, target=3)
        arr[values[3]] = values[1] + values[2]
        pointer += 4
        return arr, pointer, True

    def opcode02(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=4, target=3)
        arr[values[3]] = values[1] * values[2]
        pointer += 4
        return arr, pointer, True

    def opcode99(self, arr, pointer, *args, **kwargs):
        pointer += 1
        return arr, pointer, False


def add_first_two_opcodes():
    opc = Opcodes()
    return {'01': opc.opcode01,
            '02': opc.opcode02,
            '99': opc.opcode99}


class Intcode(object):
    """extandable compute function"""

    def __init__(self, input_name, code_length=5, function_dict=None, **kwargs):
        self.array_orig = np.loadtxt(input_name, delimiter=",", dtype=int)
        if function_dict:
            self.functions = function_dict
        else:
            self.functions = add_first_two_opcodes()
        self.kwargs = kwargs

    def get_array(self):
        return self.array_orig.copy()

    def check_code(self, code, length):
        string = f"{code:0{length}}"
        opcode = string[-2:]
        decoded = [opcode]
        for i in range(3, length+1):
            decoded.append(int(string[-i]))
        return decoded

    def compute(self, array, pointer):
        decoded = self.check_code(array[pointer], 5)
        for key, function in self.functions.items():
            if decoded[0] == key:
                return function(array, pointer, decoded, **self.kwargs)
        print(decoded[0])
        raise Exception("wrong mode")

    def get_first(self, noun, verb):
        boolean = True
        pointer = 0
        array = self.get_array()
        array[1] = noun
        array[2] = verb
        while boolean:
            array, pointer, boolean = self.compute(array, pointer)
        return array[0]

    def print_first(self, noun, verb):
        print(self.get_first(noun, verb))

    def get_noun_and_verb(self, target, range_noun=100, range_verb=100) -> (int, int):
        for noun in range(range_noun):
            for verb in range(range_verb):
                if self.get_first(noun, verb) == target:
                    return noun, verb

    def print_noun_and_verb(self, target: int, range_noun: int = 100, range_verb: int = 100):
        erg = self.get_noun_and_verb(target, range_noun=range_noun, range_verb=range_verb)
        noun = erg[0]
        verb = erg[1]
        print('Your noun has to be: ', noun)
        print('Your verb has to be: ', verb)
        print('100 * noun + verb = ', 100 * noun + verb)


if __name__ == '__main__':
    op = Opcodes()
    op_codes = {'01': op.opcode01,
                '02': op.opcode02,
                '99': op.opcode99}
    test = Intcode('../inputs/input02', function_dict=op_codes)
    test.print_first(12, 2)
    test.print_noun_and_verb(19690720)
