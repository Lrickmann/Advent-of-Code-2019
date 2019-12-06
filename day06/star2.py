from anytree.exporter import DotExporter
# graphviz needs to be installed for the next line!

from anytree import Node, RenderTree
import pandas as pd
from queue import Queue


planets = {}

test = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L","K)YOU","I)SAN"]

planets['COM'] = Node('COM')

for line in test:
    center, orbiting = line.split(")")
    planets[orbiting] = Node(orbiting, parent=planets[center])

count = 0

for planet, node in planets.items():
    count += node.depth

print(count)

san = planets['SAN']
you = planets['YOU']
you_anc = planets['YOU'].ancestors


liste = []
for planet in san.ancestors:
    if planet in you_anc:
        liste.append((san.depth-planet.depth)+(you.depth-planet.depth)-2)

print(min(liste))

planets = {}
count = 0

planets['COM'] = Node('COM')
df = pd.read_csv("../inputs/input06", delimiter=")", header=None)
df.columns = ['center', 'orbiting']
temp = Queue()
temp.put("COM")


while not df.empty:
    orbits = df[df['center'] == temp.get()]
    for i, row in orbits.iterrows():
        planets[row['orbiting']] = Node(row['orbiting'], parent=planets[row['center']])
        temp.put(row['orbiting'])
        df.drop(i, inplace=True)

for planet, node in planets.items():
    count += node.depth

print(count)

# DotExporter(planets['COM']).to_picture("orbits_from_me.png")

san = planets['SAN']
you = planets['YOU']
you_anc = planets['YOU'].ancestors


liste = []
for planet in san.ancestors:
    if planet in you_anc:
        liste.append((san.depth-planet.depth)+(you.depth-planet.depth)-2)

print(min(liste))