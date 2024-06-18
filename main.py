import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Djikstra Algo
def visitNode():
    #   1. Node with lowest distance as starting point:
    distancesNotVisited=[np.inf]*(len(distances))
    for indx in range(len(distances)):
        if isVisited[indx] == False:
            distancesNotVisited[indx] = distances[indx]

    for idHomeNode in range(len(distances)):
        if distancesNotVisited[idHomeNode] == min(distancesNotVisited):
            homeNode = chr(idHomeNode + ord('A'))
            break

    #   2. Access its neighbours nodes:
    listNeighboursId = list(zip(*np.where(connections == homeNode)))
    for (x,y) in listNeighboursId:
        if y == 0:
            neighbour = connections[x,1]
        else:
            neighbour = connections[x,0]
        edge = int(connections[x,2])
        idNeighbour = ord(neighbour) - ord('A')
        if  edge + distances[idHomeNode] < distances[idNeighbour]:
            distances[idNeighbour] = edge + distances[idHomeNode]
    isVisited[idHomeNode] = True
    return distances , isVisited


def main():
    nbNodes , nbConnections = map(int, input('Nombre de nodes, nombres de connections:   ').split(','))
    print('Les nodes sont notés avec des lettres majuscules.')
    global connections, distances, isVisited
    distances = [np.inf]*nbNodes
    isVisited = [False]*nbNodes
    
    connections = np.array([tuple(input('Node1, Node2, Distance:   ').split(',')) for _ in range(nbConnections)])

    startingNode = input('Starting node (lettre maj.):   ')
    indexStartingNode = ord(startingNode) - ord('A')
    distances[indexStartingNode] = 0

    while np.inf in distances:
        distances , isVisited = visitNode()
    
    for x in range(len(distances)):
        node = chr(x + ord('A'))
        print(startingNode, 'to', node, ':' ,distances[x])

main()