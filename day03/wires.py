import pandas as pd
import numpy as np
from enum import Enum


class Direction(Enum):
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'


class Board(object):

    def __init__(self, df: pd.DataFrame):
        self.board, self.start_pointer, self.temp_pointer = self.createNewBoard(df)
        self.crossings = {}

    """creates empty Board with maximal possible distances and resets pointer"""

    def createNewBoard(self, df: pd.DataFrame) -> (np.array, tuple, list):
        max_size_right = max(df[df['wire1_direction'] == Direction.RIGHT.value]['wire1_steps'].sum(),
                             df[df['wire2_direction'] == Direction.RIGHT.value]['wire2_steps'].sum())
        max_size_left = max(df[df['wire1_direction'] == Direction.LEFT.value]['wire1_steps'].sum(),
                            df[df['wire2_direction'] == Direction.LEFT.value]['wire2_steps'].sum())
        max_size_up = max(df[df['wire1_direction'] == Direction.UP.value]['wire1_steps'].sum(),
                          df[df['wire2_direction'] == Direction.UP.value]['wire2_steps'].sum())
        max_size_down = max(df[df['wire1_direction'] == Direction.DOWN.value]['wire1_steps'].sum(),
                            df[df['wire2_direction'] == Direction.DOWN.value]['wire2_steps'].sum())

        board = np.zeros((max_size_right + max_size_left + 1, max_size_up + max_size_down + 1))
        start_pointer = (max_size_left, max_size_up)
        temp_pointer = [max_size_left, max_size_up]

        return board, start_pointer, temp_pointer

    def move_pointer(self, direction, steps):
        pass

    def mark_path(self, direction, steps):
        pass

    def check_for_crossings(self, direction, steps):
        pass


class CrossedWires(object):

    def __init__(self, input_name: str):
        self.df = pd.read_csv(input_name, delimiter=',', header=None).T
        self.df.columns = ['wire1', 'wire2']
        self.df['wire1_direction'] = self.df['wire1'].str[0].astype('category')
        self.df['wire1_steps'] = self.df['wire1'].str[1:].astype('int')
        self.df['wire2_direction'] = self.df['wire2'].str[0].astype('category')
        self.df['wire2_steps'] = self.df['wire2'].str[1:].astype('int')
        self.df.drop(columns=['wire1', 'wire2'], inplace=True)
        self.board = Board(self.df)


if __name__ == '__main__':
    wires = CrossedWires('../inputs/input03')
    print(wires.df.head())
    print(Direction.DOWN.value)
