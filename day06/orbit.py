import pandas as pd
from queue import Queue
from anytree import Node
# graphviz needs to be installed for the next line!
from anytree.exporter import DotExporter


class UniversalOrbitMap(object):

    def __init__(self, dataframe: pd.DataFrame):
        self.planets_map = {'COM': Node('COM')}
        self.df = dataframe

    @classmethod
    def from_file(cls, input_path: str) -> 'UniversalOrbitMap':
        df = pd.read_csv(input_path, delimiter=")", header=None)
        df.columns = ['center', 'orbiting']
        return cls(df)

    @classmethod
    def from_array(cls, array: list) -> 'UniversalOrbitMap':
        df = pd.read_csv(array, delimiter=")", header=None)
        df.columns = ['center', 'orbiting']
        return cls(df)

    def create_map(self):
        pass

    def get_orbital_transfers(self):
        pass


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

DotExporter(planets['COM']).to_picture("orbits_from_me.png")

san = planets['SAN']
you = planets['YOU']
you_anc = planets['YOU'].ancestors

for planet in san.ancestors[::-1]:
    if planet in you_anc:
        print((san.depth-planet.depth)+(you.depth-planet.depth)-2)
        break