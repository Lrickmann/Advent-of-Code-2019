import numpy as np
import matplotlib.pyplot as plt

startpoint = [100,100]
temppoint = [100,100]
field = np.zeros([200,200])


def resize(matrix, direct, startp,tempp, dis):
    N = np.size(matrix, 0)
    M = np.size(matrix, 1)
    b = None

    if direct == 'U':
        b = np.zeros((N+dis, M))
        b[-N:, :] = matrix
        startp[1] = startp[1] + dis
        tempp[1] = tempp[1] + dis
    elif direct == 'R':
        b = np.zeros((N, M+dis))
        b[:, :M] = matrix
    elif direct == 'D':
        b = np.zeros((N+dis, M))
        b[:N, :] = matrix
    elif direct == 'L':
        b = np.zeros((N, M+dis))
        b[:, -M:] = matrix
        startp[0] = startp[0] + dis
        tempp[0] = tempp[0] + dis

    return b, startp


def check_size(matrix, direct, steps, tempp, startp):
    if (direct == 'U') and (tempp[1]-steps < 0):
        matrix, startp = resize(matrix, direct, startp, tempp, abs(tempp[1]-steps)+1)
    elif (direct == 'R') and (tempp[0]+steps > np.size(matrix, 1)):
        matrix, startp = resize(matrix, direct, startp, tempp, abs(tempp[0]+steps)+1)
    elif (direct == 'D') and (tempp[1]+steps > np.size(matrix, 0)):
        matrix, startp = resize(matrix, direct, startp, tempp, abs(tempp[1]+steps)+1)
    elif (direct == 'L') and (tempp[0]-steps < 0):
        matrix, startp = resize(matrix, direct, startp, tempp, abs(tempp[0]-steps)+1)
    return matrix, startp


def mark_route(matrix, direction, tempp, cabelnr, startp):
    direct, steps = direction[0], int(direction[1:])

    if direct == 'U':
        matrix, startp = check_size(matrix, direct, steps, tempp, startp)
        matrix[tempp[1]-steps:tempp[1]+1, tempp[0]] = cabelnr
        tempp[1] = tempp[1] - steps
    elif direct == 'R':
        matrix, startp = check_size(matrix, direct, steps, tempp, startp)
        matrix[tempp[1], tempp[0]:tempp[0]+steps+1] = cabelnr
        tempp[0] = tempp[0] + steps
    elif direct == 'D':
        matrix, startp = check_size(matrix, direct, steps, tempp, startp)
        matrix[tempp[1]:tempp[1]+steps+1, tempp[0]] = cabelnr
        tempp[1] = tempp[1] + steps
    elif direct == 'L':
        matrix, startp = check_size(matrix, direct, steps, tempp, startp)
        matrix[tempp[1], tempp[0]-steps:tempp[0]] = cabelnr
        tempp[0] = tempp[0] - steps
    return matrix, startp, tempp


def get_manh(startp, x, y):
    x_dis = abs(startp[0]-x)
    y_dis = abs(startp[1]-y)
    return x_dis + y_dis


inputs = np.genfromtxt('../inputs/input03', dtype='str', delimiter=',')

#for dir in ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']:
#    field, startpoint, temppoint = mark_route(field, dir, temppoint, 1, startpoint)
#
#field2 = np.zeros(field.shape)
#startpoint2 = startpoint.copy()
#temppoint2 = startpoint.copy()
#distances = []
#
#for dir in ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']:
#    field2, startpoint2, temppoint2 = mark_route(field2, dir, temppoint2, 2, startpoint2)
#
#coord = []
#
#for i, row in enumerate(field):
#    for j, col in enumerate(row):
#        if field[i, j] and (field2[i - startpoint[1] + startpoint2[1], j - startpoint[0] + startpoint2[0]] == 2):
#            distances.append(get_manh(startpoint, j, i))
#            coord.append([j, i])
#
#print(min(distances))
#distances.remove(0)
#print(min(distances))

for dir in inputs[0]:
    field, startpoint, temppoint = mark_route(field, dir, temppoint, 1, startpoint)


field2 = np.zeros(field.shape)
startpoint2 = startpoint.copy()
temppoint2 = startpoint.copy()

for dir in inputs[1]:
    field2, startpoint2, temppoint2 = mark_route(field2, dir, temppoint2, 2, startpoint2)

distances = []

for i, row in enumerate(field):
    for j, col in enumerate(row):
        if field[i, j] and field2[i - startpoint[1] + startpoint2[1], j - startpoint[0] + startpoint2[0]] == 2:
            distances.append(get_manh(startpoint, j, i))

if 0 in distances:
    distances.remove(0)
print(min(distances))

plt.imsave('wire1_image.png', field)
