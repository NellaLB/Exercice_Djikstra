import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Djikstra Algo
def visitNode():
    #   1. Node with lowest distance as starting point:
    lowestDistance = min(distances)
    for idDis in range(len(distances)):
        if distances[idDis] == min(distances) and isCompletelyVisited[idDis] == False:
            idLowestDistance = idDis
            startingNode = chr(idDis + ord('A'))
            print(startingNode)
    #   2. Access its neighbours nodes:
    #       a. If neighbour node already visited but newdistance > currentdistance : pass
    #       b. Else : node + edge
    listNeighboursId = list(zip(*np.where(connections == startingNode)))
    print(listNeighboursId)


def main():
    nbNodes , nbConnections = map(int, input('Nombre de nodes, nombres de connections:   ').split(','))
    print('Les nodes sont notés avec des lettres majuscules.')
    global distances , isCompletelyVisited, connections
    distances = [np.inf]*nbNodes
    isCompletelyVisited = [False]*nbNodes
    
    connections = np.array([tuple(input('Node1, Node2, Distance:   ').split(',')) for _ in range(nbConnections)])
    print(connections, connections.ndim)

    startingNode = input('Starting node (lettre maj.):   ')
    indexStartingNode = ord(startingNode) - ord('A')
    distances[indexStartingNode] = 0

    #while np.inf in distances:
    visitNode()

main()