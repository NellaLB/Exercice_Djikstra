import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Djikstra Algo
def visitNode():
    #   1. Node with lowest distance as starting point:
    for idStartingPoint in range(len(distances)):
        if distances[idStartingPoint] == min(distances) and isVisited[idStartingPoint] == False:
            startingNode = chr(idStartingPoint + ord('A'))
    #   2. Access its neighbours nodes:
    listNeighboursId = list(zip(*np.where(connections == startingNode)))
    for x,y in listNeighboursId:
        if x == 0:
            neighbour = connections[x,1]
        else:
            neighbour = connections[x,0]
        edge = int(connections[x,2])
        idNeighbour = ord(neighbour) - ord('A')
        newDistance = edge + distances[idStartingPoint]
        if (isVisited[idNeighbour]==False) and (newDistance < distances[idNeighbour]):
            distances[idNeighbour] = newDistance
    return distances


def main():
    nbNodes , nbConnections = map(int, input('Nombre de nodes, nombres de connections:   ').split(','))
    print('Les nodes sont notés avec des lettres majuscules.')
    global distances , isVisited, connections
    distances = [np.inf]*nbNodes
    isVisited = [False]*nbNodes
    
    connections = np.array([tuple(input('Node1, Node2, Distance:   ').split(',')) for _ in range(nbConnections)])

    startingNode = input('Starting node (lettre maj.):   ')
    indexStartingNode = ord(startingNode) - ord('A')
    distances[indexStartingNode] = 0

    while np.inf in distances:
        visitNode()
    
    for x in range(len(distances)):
        node = chr(x + ord('A'))
        print(startingNode, 'to', node, ':' ,x)

main()