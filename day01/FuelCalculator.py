import pandas as pd


class FuelCalculator:

    def __init__(self, input_name):
        self.df = pd.read_csv(input_name, header=None)
        self.fuel = 0

    def calc_fuel(self, weight=None):
        if weight is None:
            weight = (self.df // 3) - 2
            self.fuel = weight.sum()[0]
            print(self.fuel)
            return self.fuel
        ret = (weight // 3) - 2
        if ret < 0:
            return 0
        return ret

    def calc_fuel_recursive(self):
        self.fuel = 0
        for index, line in self.df.iterrows():
            temp_fuel = self.calc_fuel(line[0])
            self.fuel += temp_fuel
            while temp_fuel > 0:
                temp_fuel = self.calc_fuel(temp_fuel)
                self.fuel += temp_fuel
        print(self.fuel)

    def print_fuel(self):
        print(self.fuel)


if __name__ == '__main__':
    calcfuel = FuelCalculator('input1')
    print('Fuel after creation: ')
    calcfuel.print_fuel()
    print('Calculating Fuel: ')
    calcfuel.calc_fuel()
    print('Fuel after calculation: ')
    calcfuel.print_fuel()
    print('Recursive calculating Fuel: ')
    calcfuel.calc_fuel_recursive()
    print('Fuel after recursive calculation: ')
    calcfuel.print_fuel()
