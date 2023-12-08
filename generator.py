from pyvis.network import Network
import networkx as nx

from copy import deepcopy
from random import randint

from coverage import make_coverage
from genetic import genetic_search

n = randint(3, 30)
print(f'{n=}')

g = nx.generators.trees.random_unlabeled_tree(n)

# g = nx.Graph()
# g.add_nodes_from([1, 2, 3, 4, 5, 6])
# g.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

# s = make_coverage(deepcopy(g))
s = genetic_search(g)



for i in g.nodes:
    g.nodes[i]['label'] = str(i)
    
    if i in s:
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
nt.show('nx.html', notebook=False)
