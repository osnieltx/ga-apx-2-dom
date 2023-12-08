import os
import pickle
import time
from copy import deepcopy

import networkx as nx
from pyvis.network import Network
from tqdm import tqdm

from coverage import make_coverage
from genetic import genetic_search

data_in = "./results_2/"
data_out = "./results_5/"

def save(g, s, key):
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
    nt.show(f'{data_in}{n}_{key}.html', notebook=False)


for filename in tqdm(os.listdir(data_in)):
    if filename.endswith('.graphml'):
        file_path = os.path.join(data_in, filename)
        g = nx.read_graphml(file_path)
        n = filename.split('.')[0]
        print(f"---------- {n}")
        
        c_s = time.process_time()
        s_carmen = make_coverage(deepcopy(g))
        # save(g, s_carmen, 'alg')
        c_t = time.process_time() - c_s


        g_s = time.process_time()
        s_genetic = genetic_search(g)
        # save(g, s_genetic, 'gen')
        g_t = time.process_time() - g_s

        result = {'alg': s_carmen, 'alg_t':c_t, 'gen': s_genetic, 'gen_t': g_t}
        with open(f"{data_out}{n}.pkl", 'wb') as f:
            pickle.dump(result, f)

        # print(f"{time.process_time()-c_s:.2f}")



