import networkx as nx
import numpy as np
import matplotlib as plt


nbNodes = int(input('Nombre de nodes:  '))
nbConnections = int(input('Nombre de connections:  '))

distances = ['inf']*nbNodes
connections = []
for _ in range(nbConnections):
    connections.append(int(input()))

graphe.add_nodes_from(nbNodes)
graphe.add_edges_from(connections)
plt.show()

startingNode = int(input('Source node:  '))
distances[startingNode-1] = 0

#Djikstra Algo
def visitNode():
    #   1. Access neighbours nodes:
    #       a. If neighbour node already visited & distance node + neighbour < neighbour : node + neighbour
    #       b. Else set his distance to : edge + node
    #   2. Node with lowest distance as new starting point
    pass

while 'inf' in distances:
    visitNode()