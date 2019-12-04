import pandas as pd
import numpy as np
from enum import Enum
from matplotlib import pyplot as plt
from matplotlib import colors
from os import path


class Direction(Enum):
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'


class Board(object):

    def __init__(self, df: pd.DataFrame):
        self.board, self.start_pointer, self.temp_pointer = self.createNewBoard(df)

    """creates empty Board with maximal possible distances, so we dont need to resize and resets pointer"""
    def createNewBoard(self, df: pd.DataFrame) -> (np.array, tuple, list):
        max_size_right = max(df[df['wire1_direction'] == Direction.RIGHT.value]['wire1_steps'].sum(),
                             df[df['wire2_direction'] == Direction.RIGHT.value]['wire2_steps'].sum())
        max_size_left = max(df[df['wire1_direction'] == Direction.LEFT.value]['wire1_steps'].sum(),
                            df[df['wire2_direction'] == Direction.LEFT.value]['wire2_steps'].sum())
        max_size_up = max(df[df['wire1_direction'] == Direction.UP.value]['wire1_steps'].sum(),
                          df[df['wire2_direction'] == Direction.UP.value]['wire2_steps'].sum())
        max_size_down = max(df[df['wire1_direction'] == Direction.DOWN.value]['wire1_steps'].sum(),
                            df[df['wire2_direction'] == Direction.DOWN.value]['wire2_steps'].sum())

        board = np.zeros((max_size_right + max_size_left + 1, max_size_up + max_size_down + 1), dtype=int)
        start_pointer = (max_size_left, max_size_up)
        temp_pointer = [max_size_left, max_size_up]

        return board, start_pointer, temp_pointer

    """resets temp_pointer back to the starting point"""
    def reset_temp_pointer(self):
        self.temp_pointer = list(self.start_pointer)

    def move_pointer(self, direction):
        if direction == Direction.UP.value:
            self.temp_pointer[1] -= 1
        elif direction == Direction.RIGHT.value:
            self.temp_pointer[0] += 1
        elif direction == Direction.DOWN.value:
            self.temp_pointer[1] += 1
        elif direction == Direction.LEFT.value:
            self.temp_pointer[0] -= 1

    def mark_path(self, wire: int):
        current_pos = tuple(self.temp_pointer)
        current_value = self.board[current_pos]
        if current_value == 0 or current_value == wire:
            self.board[current_pos] = wire
        else:
            self.board[current_pos] = -1

    def walk_path(self, direction: str, steps: int, wire: int, mark: bool = True, distance: int = None,
                  distances_dict: dict = None):
        for s in range(steps):
            self.move_pointer(direction)
            if mark:
                self.mark_path(wire)
            else:
                distance += 1
                distance, distances_dict = self.check_crossing(distance, distances_dict)
        if not mark:
            return distance, distances_dict

    def check_crossing(self, distance: int, distances_dict: dict):
        current_pos = tuple(self.temp_pointer)
        current_value = self.board[current_pos]
        if current_value == -1:
            if current_pos not in distances_dict:
                distances_dict[current_pos] = distance
            else:
                distances_dict[current_pos] += distance
        return distance, distances_dict

    def get_closest_point(self):
        crossings = np.argwhere(self.board == -1)
        distances = {}
        for cross in crossings:
            distances[tuple(cross)] = self._get_manhattan_distance(cross[0], cross[1])
        coord = min(distances, key=distances.get)
        distance = distances[coord]
        return coord, distance

    def _get_manhattan_distance(self, x, y):
        x_dis = abs(self.start_pointer[0] - x)
        y_dis = abs(self.start_pointer[1] - y)
        return x_dis + y_dis

    def draw_wires(self, path):
        cmap = colors.ListedColormap(['w', 'g', 'b', 'r'])
        plt.imsave(path, self.board, cmap=cmap)


class CrossedWires(object):

    def __init__(self, input_name: str):
        self.df = pd.read_csv(input_name, delimiter=',', header=None).T
        self.wires = np.array(self.df.columns) + 1
        for i in self.wires:
            self.df[f'wire{i}_direction'] = self.df[i - 1].str[0].astype('category')
            self.df[f'wire{i}_steps'] = self.df[i - 1].str[1:].astype('int')
        self.df.drop(columns=self.wires - 1, inplace=True)
        self.board = Board(self.df)
        for i in self.wires:
            self.add_wire(i)

    def add_wire(self, wire):
        self.board.reset_temp_pointer()
        for row in range(len(self.df)):
            self.board.walk_path(self.df[f'wire{wire}_direction'][row],
                                 self.df[f'wire{wire}_steps'][row], wire)

    def get_fewest_combined_steps(self) -> (tuple, int):
        crossing_distances = {}
        for wire in self.wires:
            self.board.reset_temp_pointer()
            distance = 0
            for row in range(len(self.df)):
                distance, crossing_distances = self.board.walk_path(self.df[f'wire{wire}_direction'][row],
                                                                    self.df[f'wire{wire}_steps'][row], wire, mark=False,
                                                                    distance=distance,
                                                                    distances_dict=crossing_distances)
        if len(crossing_distances) == 0:
            raise Exception("There are no crossings. Did you add the wires first?")
        coord = min(crossing_distances, key=crossing_distances.get)
        distance = crossing_distances[coord]
        return coord, distance

    def print_fewest_combined_steps(self):
        coord, distance = self.get_fewest_combined_steps()
        print(f"The crossing Point with the fewest combined steps is on Position "
              f"{np.array(coord) - np.array(self.board.start_pointer)} with a combined distance of {distance}")

    def print_closest_point(self):
        coord, distance = self.board.get_closest_point()
        print(f"The crossing Point with the lowest Manhattan Distance is on Position "
              f"{np.array(coord) - np.array(self.board.start_pointer)} with a Manhattan distance of {distance}")

    def draw_wires(self, path):
        self.board.draw_wires(path)


if __name__ == '__main__':
    image_name = 'image_wires.png'
    wires = CrossedWires('../inputs/input03')
    wires.print_closest_point()
    wires.print_fewest_combined_steps()
    # if not path.exists(image_name):
    #     print("printing Image")
    #     wires.draw_wires(image_name)
    print("finished")
