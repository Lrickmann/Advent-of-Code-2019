from day02.intcode import Intcode as Intc, Opcodes as Opc


class Opcodes(Opc):

    def opcode03(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=1)
        if 'user_input' not in kwargs:
            raise Exception("There is no user input")
        else:
            arr[values[1]] = kwargs['user_input']
        pointer += 2
        return arr, pointer, True

    def opcode04(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=2)
        print(values[1])
        pointer += 2
        return arr, pointer, True

    def opcode05(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=3, target=3)
        if not values[1]:
            pointer += 3
        else:
            pointer = values[2]
        return arr, pointer, True

    def opcode06(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=3, target=3)
        if not values[1]:
            pointer = values[2]
        else:
            pointer += 3
        return arr, pointer, True

    def opcode07(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=4, target=3)
        if values[1] < values[2]:
            arr[values[3]] = 1
        else:
            arr[values[3]] = 0
        pointer += 4
        return arr, pointer, True

    def opcode08(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=4, target=3)
        if values[1] == values[2]:
            arr[values[3]] = 1
        else:
            arr[values[3]] = 0
        pointer += 4
        return arr, pointer, True


class Intcode(Intc):

    def print_diagnostic_code(self):
        boolean = True
        pointer = 0
        array = self.get_array()
        while boolean:
            array, pointer, boolean = self.compute(array, pointer)


if __name__ == '__main__':
    user_var = True
    op = Opcodes()
    print("test01: ", op.opcode01([1101, 100, -1, 4, 0], 0, ['01', 1, 1, 0]))
    print("test03: ", op.opcode03([3, 0, 4, 0, 99], 0, ['03', 0, 0, 0], user_input=1))
    print("test04: ", op.opcode04([3, 0, 4, 0, 99], 2, ['04', 0, 0, 0], user_input=1))
    op_codes = {'01': op.opcode01,
                '02': op.opcode02,
                '03': op.opcode03,
                '04': op.opcode04,
                '05': op.opcode05,
                '06': op.opcode06,
                '07': op.opcode07,
                '08': op.opcode08,
                '99': op.opcode99}
    test = Intcode(function_dict=op_codes)
    test.load_input('../inputs/input02')
    test.print_first(12, 2)
    test.print_noun_and_verb(19690720)
    while user_var:
        print("please give an input: ")
        user_var = int(input())
        test = Intcode(function_dict=op_codes, user_input=user_var)
        test.load_array([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
        test.print_diagnostic_code()
        if user_var == 5:
            test2 = Intcode(function_dict=op_codes, user_input=user_var)
            test2.load_input('../inputs/input05')
            test2.print_diagnostic_code()
