import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

distances = []
nbNodes , nbConnections = map(int, input('Nombre de nodes, nombres de connections:   ').split(','))
print('Les nodes sont notés avec des lettres majuscules.')

connections = np.array([tuple(input('Node1, Node2, Distance:   ').split(',')) for _ in range(nbConnections)])
print(connections, connections.ndim)

#Djikstra Algo
def visitNode():
    #   1. Node with lowest distance as new starting point
    #   2. Access its neighbours nodes:
    #       a. If neighbour node already visited but newdistance > currentdistance : pass
    #       b. Else : node + edge
    #   3. Loop
    pass

while 'inf' in distances:
    visitNode()