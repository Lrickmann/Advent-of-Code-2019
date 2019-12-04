import cosmetics as c
from day01.fuel import FuelCalculator
from day02.intcode import Intcode
from day03.wires import CrossedWires

c.print_header()
days = c.next_day()

print(next(days))
day01 = FuelCalculator('inputs/input01')
day01.calc_fuel()
day01.calc_fuel_recursive()

print(next(days))
day02 = Intcode('inputs/input02')
day02.get_first(12, 2)
day02.get_noun_and_verb()

print(next(days))
day03 = CrossedWires('inputs/input03')
day03.print_closest_point()
day03.print_fewest_combined_steps()
