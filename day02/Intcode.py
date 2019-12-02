import numpy as np


class Intcode:

    def __init__(self, input_name, func_mode=None, func=None):
        self.array_orig = np.loadtxt(input_name, delimiter=",", dtype=int)
        self.compute_func_mode = func_mode
        self.compute_func = func

    """
        Berechnet den nächsten Schritt, abhängig vom mode.
        Kann eine im Konstruktor definierte Formel übernehmen und anwenden
    """
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
            arr = self.compute_func( arr, mode, first, second, target)
            return arr, True
        else:
            print(mode)
            raise Exception("falscher mode")

    def get_noun_and_verb(self):
        done = False
        counter = 4

        for noun in range(100):
            for verb in range(100):
                boolean = True
                i = 0
                array = self.array_orig.copy()
                array[1] = noun
                array[2] = verb
                while boolean:
                    if array[i] == 99:
                        i += 1
                        boolean = False
                    else:
                        array, boolean = self.compute(array, array[i], array[i+1], array[i+2], array[i+3])
                        i += counter
                if array[0] == 19690720:
                    print('noun: ', noun)
                    print('verb: ', verb)
                    print('100 * noun + verb', 100 * noun + verb)
                    done = True
                    break
            if done:
                break

    def get_first(self, noun, verb):
        boolean = True
        i = 0
        array = self.array_orig
        array[1] = noun
        array[2] = verb
        while boolean:
            array, boolean = self.compute(array, array[i], array[i + 1], array[i + 2], array[i + 3])
            i += 4
        print(array[0])


if __name__ == '__main__':
    test = Intcode('input2')
    test.get_noun_and_verb()
    test.get_first(12, 2)
