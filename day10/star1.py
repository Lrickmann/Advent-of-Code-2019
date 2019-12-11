import numpy as np
from sympy import Point, Line#
from io import StringIO
size = 20

test = u".#..##.###...#######\n" \
       u"##.############..##.\n" \
       u".#.######.########.#\n" \
       u".###.#######.####.#.\n" \
       u"#####.##.#.##.###.##\n" \
       u"..#####..#.#########\n" \
       u"####################\n" \
       u"#.####....###.#.#.##\n" \
       u"##.#################\n" \
       u"#####.##.###..####..\n" \
       u"..######..##.#######\n" \
       u"####.##.####...##..#\n" \
       u".#####..#.######.###\n" \
       u"##...#.##########...\n" \
       u"#.##########.#######\n" \
       u".####.#.###.###.#.##\n" \
       u"....##.##.###..#####\n" \
       u".#.#.###########.###\n" \
       u"#.#.#.#####.####.###\n" \
       u"###.##.####.##.#..##\n"
field = np.genfromtxt(StringIO(test), delimiter=[1] * size, comments=None, dtype=int,
                      converters={key: lambda x: 1 if x == b'#' else 0 for key in range(size)})

positions = [Point(x, y) for x, y in np.argwhere(field == 1)]
field3D = field * field[:, :, np.newaxis]

print(field3D[2])

lines = np.argwhere(field3D == 1)
field3D = field3D.astype('object')
for z, x, y in lines:
    if y <= z:
        field3D[z, x, y] = 0
    else:
        field3D[z, x, y] = Line(Point(x, y), Point(x, z))
print(lines[1])
print(field3D[0, 3, 1])

paths = np.argwhere(field3D != 0)
print(paths[0])
paths_len = len(paths)
visible_comets = {}
min_blocked = paths_len
progress = 0

for point in positions:
    blocked_counter = 0
    for path in paths:
        if field3D[tuple(path)].contains(point):
            blocked_counter += 1
            if blocked_counter >= min_blocked:
                break
    visible_comets[point] = paths_len - 1 - blocked_counter
    if visible_comets[point] < min_blocked:
        min_blocked = visible_comets[point]
    progress += 1
    print("%02d" % (progress/len(positions)*100))

print(visible_comets)
print(max(visible_comets, key=visible_comets.get))
