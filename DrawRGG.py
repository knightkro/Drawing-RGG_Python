# -*- coding: utf-8 -*-


# Draw a random geometric graph using python's networkx package




###############################################################################
# Import the necessary packages:
#
#
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math, random
#
#
###############################################################################




###############################################################################
# Some functions we will use :
#
#
def RGG_nodes(nodes,dim): #returns a set of nodes randomly distributed in the unit cube
    Nod=nx.Graph()
    Nod.add_nodes_from(range(nodes))
    for n in Nod:
        Nod.node[n]['pos']=[random.random() for i in range(0,dim)]
    return Nod

def RGG_edges(Nodeset,r): #take a set of nodes (Nodeset) and add edges to create a RGG with connection radius r    
    nodes = Nodeset.nodes(data=True)
    while nodes:
        u,du = nodes.pop()
        pu = du['pos']
        for v,dv in nodes:
            pv = dv['pos']
            d = sum(((a-b)**2 for a,b in zip(pu,pv)))
            if d <= r**2:
                Nodeset.add_edge(u,v)
    return Nodeset 
#
#
###############################################################################


###############################################################################
# Parameters
#
#
Number_nodes = 1000 # choose the number of nodes
dimens = 2 # Set the dimension to two!
connect_radius = 0.14 # Choose the connection radius
#
#
###############################################################################
    
    
###############################################################################
# Draw the network
#
#    
Our_nodes = RGG_nodes(Number_nodes,dimens) 
RGG_edges(Our_nodes,connect_radius)
posg = nx.get_node_attributes(Our_nodes,'pos')
im=nx.draw_networkx_nodes(Our_nodes,posg,node_size=15,alpha = 0.6, node_color='b')
nx.draw_networkx_edges(Our_nodes,posg,alpha=0.1) 
plt.xlim(-0.01,1.01)
plt.ylim(-0.01,1.01)
#
#
