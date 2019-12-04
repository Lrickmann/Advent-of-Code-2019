import numpy as np

pw_range = np.loadtxt('../inputs/input04', delimiter='-').astype('int')

pws=[]

def check_pw(number):
    pw = str(number)
    doubles = False
    for i, c in enumerate(pw):
        if i == 0:
            continue
        if c < pw[i-1]:
            return False
        elif c == pw[i-1]:
            doubles = True
    if doubles:
        return True
    return False

for i in range(pw_range[0], pw_range[1]):
    if check_pw(i):
        pws.append(i)

print(len(pws))