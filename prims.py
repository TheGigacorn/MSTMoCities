import math
import sys
from collections import defaultdict
import heapq
class Graph():
    def __init__(self, verticies):
        self.V = verticies
        self.graph = [[0 for x in range(verticies)] for y in range(verticies)]

    def printMST(self, parent):
        printList = defaultdict(list)
        #print(self.graph)
        print("Edge \tWeight")
        for i in range (1,self.V):
                print(cityname[parent[i]],"-",cityname[i],"\t",self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        minimum = float("inf")
        for v in range(self.V):
            if key[v] < minimum and mstSet[v] == False:
                minimum = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [float("inf")] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)

filearray = []
cityname = []
population = []
latitude = []
longitude = []
distance = []
R = 3961
with open("mocities.dat","r") as data:
    for x in data:
        filearray.append(x)
    for y in filearray:
        if y.find(',') != -1:
            cityname.append(y[:y.find(',')])
        if y.find('+') != -1:
            population.append(y[:y.find('+')-1])
            latitude.append(y[y.find('+')+1:y.find('+')+3] + '.' + y[y.find('+')+3:y.find('-')-1])
            longitude.append(y[y.find('-'):y.find('-')+4] + '.' + y[y.find('-')+4:y.find('\n')])
data.close()

#       Equation that converts lat-long to distance in miles        #
adjacencyMat = [[0 for i in range(len(latitude))] for j in range(len(longitude))]
adjacencyList = defaultdict(list)
for i in range(0, len(latitude)):
    for j in range(0, len(longitude)):
        p = 0.017453292519943295     #Pi/180
        a = 0.5 - math.cos((float(latitude[j]) - float(latitude[i])) * p)/2 + math.cos(float(latitude[i]) * p) * math.cos(float(latitude[j])* p) * (1 - math.cos((float(longitude[j]) - float(longitude[i])) * p)) / 2
        d= 7922 * math.asin(math.sqrt(a))
        if d <= 30:
            adjacencyMat[i][j] = d
            newNode = [cityname[j], d]
            adjacencyList[i].insert(0, newNode)

for i in adjacencyList:
    print('#{}: {}\n'.format(cityname[i], adjacencyList[i]))
#print(cityname)
#print(population)
#print(latitude)
#print(longitude) 

g = Graph(len(cityname))
g.graph = adjacencyMat
g.primMST()
