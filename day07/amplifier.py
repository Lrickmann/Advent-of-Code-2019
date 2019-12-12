from day05.intcode import Intcode as Inc, Opcodes as Opc


class Opcodes(Opc):

    def opcode_amp_03(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=1)
        if 'user_input' not in kwargs:
            raise Exception("There is no user input")
        else:
            arr[values[1]] = kwargs['phase']
            kwargs['phase'] = kwargs['user_input']
        pointer += 2
        return arr, pointer, True

    def opcode_amp_04(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=2)
        print(values[1])
        pointer += 2
        return values[1], pointer, False


class Intcode(Inc):

    def get_amp_code(self):
        out = None
        boolean = True
        pointer = 0
        array = self.get_array()
        while boolean:
            out, pointer, boolean = self.compute(array, pointer)
        return out


class Amplifier:

    def __init__(self, input_path, opcodes, phase):
        self.intcode = Intcode(function_dict=opcodes, phase=phase).load_input(input_path)

    def get_output(self, amp_input):
        self.intcode.kwargs['user_input'] = amp_input
        return self.intcode.get_amp_code()


class AmplificationCircuit:

    def __init__(self, number_amp, input_path, opcodes, phaselist):
        self.amplifier = [Amplifier(input_path, opcodes, phaselist[_]) for _ in range(number_amp)]

    def run_amplifier(self, init_val):
        signal = init_val
        for amplifier in self.amplifier:
            signal = amplifier.get_output(signal)
        return signal

    def create_signals(self):
        pass

    def run_signals(self):
        pass

    def find_highest_thrust(self):
        pass

if __name__ == '__main__':
    op = Opcodes()
    op_codes = {'01': op.opcode01,
                '02': op.opcode02,
                '03': op.opcode03,
                '04': op.opcode04,
                '05': op.opcode05,
                '06': op.opcode06,
                '07': op.opcode07,
                '08': op.opcode08,
                '99': op.opcode99}
    test = Intcode(function_dict=op_codes, user_input=0)
    test.load_input('../inputs/input07')
    test.print_diagnostic_code()

    amp_circut = AmplificationCircuit(5, '../inputs/input07', op_codes)
