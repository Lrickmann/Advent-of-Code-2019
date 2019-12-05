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
        values = self.get_values(arr, pointer, codes, length=2, target=1)
        print(values[1])
        pointer += 2
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
    while user_var:
        print("please give an input: ")
        user_var = int(input())
        op = Opcodes()
        print("test01: ", op.opcode01([1101, 100, -1, 4, 0], 0, ['01', 1, 1, 0]))
        print("test03: ", op.opcode03([3,0,4,0,99], 0, ['03', 1, 1, 0], user_input=1))
        op_codes = {'01': op.opcode01,
                    '02': op.opcode02,
                    '03': op.opcode03,
                    '04': op.opcode04,
                    '99': op.opcode99}
        test = Intcode('../inputs/input02', function_dict=op_codes)
        test.print_first(12, 2)
        test.print_noun_and_verb(19690720)
        test2 = Intcode('../inputs/input05', function_dict=op_codes, user_input=user_var)
        test2.print_diagnostic_code()
