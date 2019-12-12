import cosmetics as c
from day01.fuel import FuelCalculator
from day02.intcode import Intcode as Intcode02, Opcodes as Opcodes02
from day03.wires import CrossedWires
from day04.password import Password
from day05.intcode import Intcode as Intcode05, Opcodes as Opcodes05

c.print_header()
days = c.next_day()

print(next(days))
day01 = FuelCalculator('inputs/input01')
day01.calc_fuel()
day01.calc_fuel_recursive()

print(next(days))
op = Opcodes02()
op_codes02 = {'01': op.opcode01,
              '02': op.opcode02,
              '99': op.opcode99}
day02 = Intcode02(function_dict=op_codes02)
day02.load_input('inputs/input02')
day02.print_first(12, 2)
day02.print_noun_and_verb(19690720)

print(next(days))
#day03 = CrossedWires('inputs/input03')
#day03.print_closest_point()
#day03.print_fewest_combined_steps()

print(next(days))
day04 = Password('inputs/input04')
day04.count_passwords_with_multiples()
day04.count_passwords_with_doubles()

print(next(days))
op = Opcodes05()
op_codes05 = {'01': op.opcode01,
              '02': op.opcode02,
              '03': op.opcode03,
              '04': op.opcode04,
              '05': op.opcode05,
              '06': op.opcode06,
              '07': op.opcode07,
              '08': op.opcode08,
              '99': op.opcode99}
day05 = Intcode05(function_dict=op_codes05, user_input=1)
day05.load_input('inputs/input05')
day05.print_diagnostic_code()
day05.kwargs['user_input'] = 5
day05.print_diagnostic_code()

