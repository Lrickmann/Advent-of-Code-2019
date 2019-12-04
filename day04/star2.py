import numpy as np

pw_range = np.loadtxt('../inputs/input04', delimiter='-').astype('int')

pws=[]

def check_pw(number):
    pw = str(number)
    for i, c in enumerate(pw):
        if i == 0:
            continue
        if c < pw[i-1]:
            return False

    for i in range(10):
        x = pw.count(str(i))
        if x == 2:
            return True
    return False

for i in range(pw_range[0], pw_range[1]):
    if check_pw(i):
        pws.append(i)

print(len(pws))