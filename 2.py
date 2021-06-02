# https://colab.research.google.com/drive/1KI-sanhyNH1gyMoqnODFBJfSruevKsJd#scrollTo=TjZ3Tn4KFMin

import networkx as nx
import matplotlib.pyplot as plt
from random import randint
g = nx.Graph()
 
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
colors = ["BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK","BLACK", "BROWN", "WHITE", "PURPLE"]
 
for edge in edges:
    g.add_edge(edge[0],edge[1])
 
# g = edge_allocated(g, edges)
 
color = nx.coloring.greedy_color(g, strategy = "largest_first")
 
v_color = [colors[color[edge]] for edge in sorted(color)]
e_color = [colors[randint(0,9)] for edge in sorted(color)]
f_color = [colors[color[edge]+4] for edge in sorted(color)]
nx.draw(g, node_color = v_color, edge_color=e_color ,with_labels = True, width=3, node_size=400)
 
for index,color in enumerate(v_color):
    print("Color assigned to vertex", index, "is", color)
print("*-------------------------------------*")
for index,color in enumerate(e_color):
    print("Color assigned to Edge", index, "is", color)
print("*-------------------------------------*")
for index,color in enumerate(f_color):
    print("Color assigned to Face", index, "is", color)



""" 
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Polygon
import numpy as np

G = nx.Graph()

colors = {0:"red", 1:"green", 2:"blue", 3:"yellow"}

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (1,3), (2,4), (3,4), (4,5)])

nodes = list(G.nodes)
edges = list(G.edges)

color_lists = []
color_of_edge = []
some_colors = ['red','green','blue','yellow']

for i in range(len(nodes) + 1):
    color_lists.append([])
    color_of_edge.append(-1)

def getSmallestColor(ls1,ls2):
    i = 1
    while(i in ls1 or i in ls2):
        i = i + 1
    return i

#iterate over edges
i = 0
for ed in edges:
    newColor = getSmallestColor(color_lists[ed[0]],color_lists[ed[1]])
    color_lists[ed[0]].append(newColor)
    color_lists[ed[1]].append(newColor)
    color_of_edge[i] = newColor
    i = i + 1

# Makin graph again
G = nx.Graph()

for i in range(len(edges)):
    G.add_edge(edges[i][0],edges[i][1],color=some_colors[color_of_edge[i]-1])

colors = nx.get_edge_attributes(G,'color').values()
nx.draw(G, edge_color=colors, with_labels=True, width=2)
"""
