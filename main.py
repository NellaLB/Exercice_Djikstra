import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


nbNodes = int(input('Nombre de nodes:  '))
nbConnections = int(input('Nombre de connections:  '))

distances = ['inf']*nbNodes
connections = np.array([], ndmin=1)
for _ in range(nbConnections):
    newConnections = np.array(map(int, input('Node en lettre majuscule:   ').split(',')), ndmin=1)
    np.concatenate((connections, newConnections), axis=0)
listNodes =[]

graph = nx.Graph()
graph.add_nodes_from(listNodes)
graph.add_edges_from(connections)

plt.figure()
nx.draw(graph)
plt.show()

startingNode = int(input('Source node:  '))
distances[ord(startingNode)-ord('A')-1] = 0

#Djikstra Algo
def visitNode():
    #   1. Access its neighbours nodes:
    #       a. If neighbour node already visited & distance node + neighbour < neighbour : node + neighbour
    #       b. Else set his distance to : edge + node
    #   2. Node with lowest distance as new starting point
    #   3. Loop
    pass

while 'inf' in distances:
    visitNode()