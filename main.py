import numpy as np
import pandas as pd

#Djikstra Algo
def visitNode():
    #   1. Node with lowest distance as starting point:
    distancesNotVisited = [np.inf]*(nbNodes)
    for indx in range(nbNodes):
        if isVisited[indx] == False:
            distancesNotVisited[indx] = distances[indx]

    for idHomeNode in range(nbNodes):
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
    try:
        #Import CSV file
        fileName = input('Insérer le nom d\'un fichier CSV:  ')
        fileCSV = pd.read_csv(fileName)
        fileCSV = pd.DataFrame(fileCSV)

        #Data cleaning
        fileCSV.drop_duplicates(subset=['Node1','Node2'], inplace=True)
        fileCSV.dropna(inplace=True)

        global connections, distances, isVisited, nbNodes
        nbNodes = len(set(fileCSV.Node1) | set(fileCSV.Node2))
        distances = [np.inf]*nbNodes
        isVisited = [False]*nbNodes
        
        connections = fileCSV.to_numpy()

        startingNode = input('Starting node from A to ' + chr(nbNodes + ord('A') - 1) + ':   ')
        indexStartingNode = ord(startingNode) - ord('A')
        distances[indexStartingNode] = 0

        #Visites des nodes (djikstra algo)
        while (np.inf in distances) or (False in isVisited):
            distances , isVisited = visitNode()

        #Affichage des valeurs
        for x in range(nbNodes):
            node = chr(x + ord('A'))
            print(startingNode, 'to', node, ':' ,distances[x])
    except:
        print('On dirait qu\'il y a eu une erreur. Réessayer.')
        main()
main()