from itertools import combinations
import numpy as np
from math import gcd
import re
import time

class OrbitalMotion:

    def __init__(self):
        self.planets = []
        self.step_counter = 0

    def read_input(self, input_path):
        with open(input_path, 'r') as f:
            for line in f:
                self.planets.append(Moon(line))

    def read_string(self, string):
        lines = string.split('\n')
        for line in lines:
            self.planets.append(Moon(line))

    def apply_gravity(self):
        for moon1, moon2 in combinations(self.planets, 2):
            moon1.calculate_velocity(moon2)
            moon2.calculate_velocity(moon1)

    def apply_velocity(self):
        for moon in self.planets:
            moon.apply_velocity()

    def make_step(self):
        self.apply_gravity()
        self.apply_velocity()
        self.step_counter += 1

    def run_n_steps(self, steps, print_range):
        self.print_step()
        for _ in range(steps):
            if _ % print_range == 0 and print_range != steps:
                self.print_step()
            self.make_step()
        self.print_step()
        self.print_energy()
        print("------------------------------------------------")

    def run_inital_state(self, print_range=1_000_000):
        init_states = np.array([0, 0, 0], dtype='object')
        # init_count = np.array([1, 1, 1])
        while 0 in init_states:
            self.make_step()
            if self.get_universe_state_x() and init_states[0] == 0:
                print(f"X Coord repeats after {self.step_counter} steps")
                init_states[0] = self.step_counter
            if self.get_universe_state_y() and init_states[1] == 0:
                print(f"Y Coord repeats after {self.step_counter} steps")
                init_states[1] = self.step_counter
            if self.get_universe_state_z() and init_states[2] == 0:
                print(f"Z Coord repeats after {self.step_counter} steps")
                init_states[2] = self.step_counter
        init_step = np.lcm.reduce(init_states)
        print(f"Universe repeated after {init_step} steps")
        print("------------------------------------------------")

    def print_step(self):
        print(f'After {self.step_counter} steps:')
        [moon.print_state() for moon in self.planets]

    def print_energy(self):
        [moon.print_energy() for moon in self.planets]
        energy = [moon.get_total_energy() for moon in self.planets]
        print(f'Sum of total energy: {energy[0]:3} + {energy[1]:3} + {energy[2]:3} + {energy[3]:3} = {sum(energy):3}')

    def get_universe_state_x(self):
        return np.prod([moon.initial_state_x() for moon in self.planets])

    def get_universe_state_y(self):
        return np.prod([moon.initial_state_y() for moon in self.planets])

    def get_universe_state_z(self):
        return np.prod([moon.initial_state_z() for moon in self.planets])


class Moon:

    def __init__(self, input_string):
        regex = re.compile("\w=-?\d*")
        positions = regex.findall(input_string)
        self.pos_x = int(positions[0][2:])
        self.pos_y = int(positions[1][2:])
        self.pos_z = int(positions[2][2:])
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        self.initial_position = self.get_moon_state()

    def get_moon_state(self):
        return self.pos_x, self.pos_y, self.pos_z, self.vel_x, self.vel_y, self.vel_z,

    def compare_position(self, own, other):
        return 1 if own < other else -1 if own > other else 0

    def calculate_velocity(self, other_moon):
        self.vel_x += self.compare_position(self.pos_x, other_moon.pos_x)
        self.vel_y += self.compare_position(self.pos_y, other_moon.pos_y)
        self.vel_z += self.compare_position(self.pos_z, other_moon.pos_z)

    def apply_velocity(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def get_potential_energy(self):
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    def get_kinetic_energy(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    def initial_state_x(self):
        return True if self.initial_position[0] == self.get_moon_state()[0] and self.initial_position[3] == \
                       self.get_moon_state()[3] else False

    def initial_state_y(self):
        return True if self.initial_position[1] == self.get_moon_state()[1] and self.initial_position[4] == \
                       self.get_moon_state()[4] else False

    def initial_state_z(self):
        return True if self.initial_position[2] == self.get_moon_state()[2] and self.initial_position[5] == \
                       self.get_moon_state()[5] else False

    def print_energy(self):
        print(
            f"pot:  {abs(self.pos_x):3} + {abs(self.pos_y):3} + {abs(self.pos_z):3} = {self.get_potential_energy():3};"
            f"   kin: {abs(self.vel_x):3} + {abs(self.vel_y):3} + {abs(self.vel_z):3} = {self.get_kinetic_energy():3};"
            f"   total: {self.get_potential_energy():3} * {self.get_kinetic_energy():3} = {self.get_total_energy():3}")

    def print_state(self):
        print(f'pos=<x={self.pos_x:3}, y={self.pos_y:3}, z={self.pos_z:3}>,'
              f'vel=<x={self.vel_x:3}, y={self.vel_y:3}, z={self.vel_z:3}>')


if __name__ == '__main__':
    print("Run Testinput 1: ")
    test = "<x=-1, y=0, z=2>\n" \
           "<x=2, y=-10, z=-7>\n" \
           "<x=4, y=-8, z=8>\n" \
           "<x=3, y=5, z=-1>"
    test_orbit = OrbitalMotion()
    test_orbit.read_string(test)
    test_orbit.run_n_steps(10, 10)
    test_orbit = OrbitalMotion()
    test_orbit.read_string(test)
    test_orbit.run_inital_state()

    print("\n\nRun Testinput 1: ")
    test2 = "<x=-8, y=-10, z=0>\n" \
            "<x=5, y=5, z=10>\n" \
            "<x=2, y=-7, z=3>\n" \
            "<x=9, y=-8, z=-3>"
    test_orbit2 = OrbitalMotion()
    test_orbit2.read_string(test2)
    test_orbit2.run_n_steps(100, 100)
    test_orbit2 = OrbitalMotion()
    test_orbit2.read_string(test2)
    test_orbit2.run_inital_state()

    print("\n\nRun actual Input: ")
    orbit = OrbitalMotion()
    orbit.read_input('../inputs/input12')
    orbit.run_n_steps(1000, 1000)
    start_time = time.time()
    orbit = OrbitalMotion()
    orbit.read_input('../inputs/input12')
    orbit.run_inital_state()
    print("--- %s seconds ---" % (time.time() - start_time))
