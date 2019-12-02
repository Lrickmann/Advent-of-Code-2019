import numpy as np


class Intcode(object):

    """extandable compute function"""
    def __init__(self, input_name, func_mode=None, func=None):
        self.array_orig = np.loadtxt(input_name, delimiter=",", dtype=int)
        self.compute_func_mode = func_mode
        self.compute_func = func

    def compute(self, arr, mode, first, second, target):
        if mode == 1:
            arr[target] = arr[first] + arr[second]
            return arr, True
        elif mode == 2:
            arr[target] = arr[first] * arr[second]
            return arr, True
        elif mode == 99:
            return arr, False
        elif self.compute_func_mode is not None and self.compute_func_mode == mode:
            arr = self.compute_func(arr, mode, first, second, target)
            return arr, True
        else:
            print(mode)
            raise Exception("falscher mode")

    def get_first(self, noun, verb, printbool=True):
        boolean = True
        i = 0
        array = self.array_orig.copy()
        array[1] = noun
        array[2] = verb
        while boolean:
            array, boolean = self.compute(array, array[i], array[i + 1], array[i + 2], array[i + 3])
            i += 4
        if printbool:
            print("Your value at position 0 is ", array[0])
        else:
            return array[0]

    def get_noun_and_verb(self):
        done = False
        for noun in range(100):
            for verb in range(100):
                if self.get_first(noun, verb, printbool=False) == 19690720:
                    print('Your noun has to be: ', noun)
                    print('Your verb has to be: ', verb)
                    print('100 * noun + verb = ', 100 * noun + verb)
                    done = True
                    break
            if done:
                break


if __name__ == '__main__':
    test = Intcode('../inputs/input02')
    test.get_first(12, 2)
    test.get_noun_and_verb()
