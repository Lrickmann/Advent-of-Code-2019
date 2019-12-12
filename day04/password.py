import numpy as np


class Password:

    def __init__(self, input_path):
        self.pw_range = np.loadtxt(input_path, delimiter='-').astype('int')
        self.pws = []

    def check_ascending(self, pw):
        for i, c in enumerate(pw):
            if i == 0:
                continue
            if c < pw[i-1]:
                return False
        return True

    def check_pw_for_multiples(self, number):
        pw = str(number)
        if self.check_ascending(pw):
            for i in range(10):
                x = pw.count(str(i))
                if x >= 2:
                    return True
        return False

    def count_passwords_with_multiples(self):
        self.pws = []
        for i in range(self.pw_range[0], self.pw_range[1]):
            if self.check_pw_for_multiples(i):
                self.pws.append(i)
        print(len(self.pws))

    def check_pw_for_doubles(self, number):
        pw = str(number)
        if self.check_ascending(pw):
            for i in range(10):
                x = pw.count(str(i))
                if x == 2:
                    return True
        return False

    def count_passwords_with_doubles(self):
        self.pws = []
        for i in range(self.pw_range[0], self.pw_range[1]):
            if self.check_pw_for_doubles(i):
                self.pws.append(i)
        print(len(self.pws))

if __name__ == '__main__':
    password = Password('../inputs/input04')
    password.count_passwords_with_multiples()
    password.count_passwords_with_doubles()
