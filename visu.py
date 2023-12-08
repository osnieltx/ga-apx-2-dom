import pickle
from pyvis.network import Network
import networkx as nx

from copy import deepcopy
from random import randint

from coverage import make_coverage
from genetic import genetic_search

n = 2048
key = 'gen'
g = nx.read_graphml(f"./results/{n}.graphml")
with open(f"./results/{n}.pkl", 'rb') as f:
    data = pickle.load(f)

s = data[key]

for i in g.nodes:
    g.nodes[i]['label'] = str(i)
    
    if int(i) in s:
        g.nodes[i]['color'] = '#fb8500'

for e in g.edges:
    g.edges[e]['color'] = 'gray'

nt = Network('1000px', '1500px')
nt.from_nx(g)

nt.toggle_physics(False)
nt.options.edges.smooth.enabled = False
nt.options.interaction.multiselect = True
nt.options.interaction.selectConnectedEdges = False

nt.show_buttons()
nt.show(f'./results/{n}_{key}.html', notebook=False)
