from day09.incode import Intcode as Intc, Opcodes as Opc
import numpy as np
import matplotlib.pyplot as plt


class Opcodes(Opc):

    def opcode_robot_04(self, arr, pointer, codes, **kwargs):
        values = self.get_values(arr, pointer, codes, length=2, target=2)
        if values[1] == 0:
            print("turning left")
        elif values[1] == 1:
            print("turning right")
        else:
            print(values[1])
        pointer += 2
        return values[1], pointer, False


class Robot(object):

    def __init__(self, intcode, startpanel=0):
        self.position = np.array([0, 0])
        self.direction = np.array([0, 1])
        self.visited = {tuple(self.position): startpanel}
        self.intcode = intcode

    def change_direction(self, rotate):
        rotation_matrix = np.array([[0, -1], [1, 0]])
        if rotate:
            rotation_matrix = rotation_matrix * -1
        self.direction = rotation_matrix.dot(self.direction)

    def change_position(self):
        self.position = self.position + self.direction
        self.scan_color()

    def paint_panel(self, color):
        self.visited[tuple(self.position)] = color

    def scan_color(self):
        if tuple(self.position) in self.visited:
            self.intcode.kwargs['user_input'] = self.visited[tuple(self.position)]
        else:
            self.intcode.kwargs['user_input'] = 0

    def move(self, color, arr):
        self.change_direction(arr)
        self.paint_panel(color)
        self.change_position()

    def print_painting(self):
        x = []
        y = []
        for point, value in self.visited.items():
            if value:
                x.append(point[0])
                y.append(point[1])
        max_p, min_p = np.max([x, y]), np.min([x, y])
        plt.scatter(x=x, y=y)
        plt.scatter(x=self.position[0], y=self.position[1], color='red')
        plt.ylim(min_p-10, max_p+10)
        plt.xlim(min_p - 10,max_p + 10)
        plt.savefig('Painting Robot.png')
        plt.show()


    def start_robot(self):
        boolean = True
        pointer = 0
        array = self.intcode.get_array()
        second = False
        while boolean:
            try:
                tmp, pointer, boolean = self.intcode.compute(array, pointer)
                if not boolean and type(tmp) == int:
                    if not second:
                        color = tmp
                        second = True
                    else:
                        self.move(color, tmp)
                        second = False
                    boolean = True


            except IndexError:
                array = np.concatenate((array, np.zeros(len(array), dtype='int64')))
        print("Robot says: 'I painted ", len(self.visited.keys()), " diffrent Panels!'")


if __name__ == '__main__':
    op = Opcodes()
    op_codes = {'01': op.opcode01,
                '02': op.opcode02,
                '03': op.opcode03,
                '04': op.opcode_robot_04,
                '05': op.opcode05,
                '06': op.opcode06,
                '07': op.opcode07,
                '08': op.opcode08,
                '09': op.opcode09,
                '99': op.opcode99}
    test = Intc(function_dict=op_codes, user_input=0)
    test.load_input('../inputs/input11')
    test.print_diagnostic_code()
    r = Robot(test)
    r.start_robot()
    r_b = Robot(test, startpanel=1)
    r_b.start_robot()
    r_b.print_painting()
