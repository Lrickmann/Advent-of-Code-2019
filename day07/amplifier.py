from day05.intcode import Intcode as Inc, Opcodes as Opc
from itertools import permutations


class Opcodes(Opc):

    def opcode_amp_03(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=1)
        if 'user_input' not in kwargs:
            raise Exception("There is no user input")
        else:
            arr[values[1]] = kwargs['phase']
        pointer += 2
        return True, pointer, True

    def opcode_amp_04(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=2)
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
            if type(out) == bool:
                self.kwargs['phase'] = self.kwargs['user_input']
        return out


class Amplifier:

    def __init__(self, input_path, opcodes, phase):
        self.intcode = Intcode(function_dict=opcodes, phase=phase, user_input=0)
        self.intcode.load_input(input_path)

    def get_output(self, amp_input):
        self.intcode.kwargs['user_input'] = amp_input
        return self.intcode.get_amp_code()


class AmplificationCircuit:

    def __init__(self, number_amp, input_path, opcodes):
        self.phase_list = self.create_phases(number_amp)
        self.number_amps = number_amp
        self.opcodes = opcodes
        self.input_path = input_path
        self.amplifier = []

    def run_amplifier_circuit(self, init_val, phases):
        self.create_circuit(phases)
        signal = init_val
        for amplifier in self.amplifier:
            signal = amplifier.get_output(signal)
        return signal

    def create_phases(self, number_amp):
        return list(permutations(range(number_amp), number_amp))

    def create_circuit(self, phases):
        self.amplifier = [Amplifier(self.input_path, self.opcodes, phase) for phase in phases]

    def find_highest_thrust(self, init_val):
        max_thrust = 0
        for phase in self.phase_list:
            thrust = self.run_amplifier_circuit(init_val, phase)
            if thrust > max_thrust:
                max_thrust = thrust
        return max_thrust


if __name__ == '__main__':
    op = Opcodes()
    op_codes = {'01': op.opcode01,
                '02': op.opcode02,
                '03': op.opcode_amp_03,
                '04': op.opcode_amp_04,
                '05': op.opcode05,
                '06': op.opcode06,
                '07': op.opcode07,
                '08': op.opcode08,
                '99': op.opcode99}
    # test = Intcode(function_dict=op_codes, user_input=0)
    # test.load_input('../inputs/input07')
    # test.print_diagnostic_code()

    amp_circut = AmplificationCircuit(5, 'testinput3', op_codes)
    amp_circut.run_amplifier_circuit(0, [1, 0, 4, 3, 2])
    amp_circut = AmplificationCircuit(5, '../inputs/input07', op_codes)
    print(amp_circut.find_highest_thrust(0))
