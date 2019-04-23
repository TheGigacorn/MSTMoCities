import math
import sys
from collections import defaultdict
import heapq
import time

        #########       MinHeap Class       ##########
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes of  
    # min heap. Needed for min heapify 
    def swapMinHeapNode(self, a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped. Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2 * idx + 1
        right = 2 * idx + 2
  
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min heap  
        # if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is not  
        # hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)/2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)/2 ) 
  
            # move to parent index 
            i = (i - 1) / 2; 
  
    # A utility function to check if a given vertex 
    # 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(parent, n): 
    for i in range(1, n): 
        print( "% d - % d" % (parent[i], i))

        #############           Adjacency list          ###########
class Graph_l(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    # Adds an edge to an undirected graph 
    def addEdge(self, src, dest, weight): 
  
        # Add an edge from src to dest.  A new node is 
        # added to the adjacency list of src. The node  
        # is added at the begining. The first element of 
        # the node has the destination and the second  
        # elements has the weight 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        # Since graph is undirected, add an edge from  
        # dest to src also 
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
    # The main function that prints the Minimum  
    # Spanning Tree(MST) using the Prim's Algorithm.  
    # It is a O(ELogV) function 
    def PrimMST(self): 
        # Get the number of vertices in graph 
        V = self.V   
          
        # key values used to pick minimum weight edge in cut 
        key = []    
          
        # List to store contructed MST 
        parent = []  
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        # Initialize min heap with all vertices. Key values of all 
        # vertices (except the 0th vertex) is is initially infinite 
        for v in range(V): 
            parent.append(-1) 
            key.append(float("inf")) 
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
            minHeap.pos.append(v) 
  
        # Make key value of 0th vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # not yet added in the MST. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
  
            # Traverse through all adjacent vertices of u  
            # (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less than 
                # its previously calculated distance 
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
                    key[v] = pCrawl[1] 
                    parent[v] = u 
  
                    # update distance value in min heap also 
                    minHeap.decreaseKey(v, key[v]) 
  
        printArr(parent, V) 


        ############        Adjacency Matrix        ###########
#The following is a series of functions that was used to calculate the MST using an adjacency matrix
class Graph_Matrix():
    def __init__(self, verticies): #creates a graph with verticies being set to the number passed to it and graph is initialized to be all 0 in a 2D matrix
        self.V = verticies
        self.graph = [[0 for x in range(verticies)] for y in range(verticies)]

    def printMST(self, parent):
        printList = defaultdict(list)
        #print(self.graph)
        print("Edge \tWeight")
        for i in range (1,self.V):
                print(parent[i])
                print(cityname[parent[i]],"-",cityname[i],"\t",self.graph[i][parent[i]])
                adjacencyMat[parent[i]][i] = self.graph[i][parent[i]]
                adjacencyListOut[parent[i]].insert(0, [cityname[i], self.graph[i][parent[i]]])

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


filearray = [] # array to hold 
cityname = []
population = []
latitude = [] #latitude and longitude are decimal degree form
longitude = []
distance = [] #distance is calculated in miles
R = 3961
with open("mocities.dat","r") as data: #opens .dat file for file reading
    for x in data:
        filearray.append(x) # appends each line into an array for easier splitting
    for y in filearray:
        if y.find(',') != -1: #if row with names
            cityname.append(y[:y.find(',')])
        if y.find('+') != -1: #if row with population, latitude, longitude
            population.append(y[:y.find('+')-1])
            latitude.append(y[y.find('+')+1:y.find('+')+3] + '.' + y[y.find('+')+3:y.find('-')-1])
            longitude.append(y[y.find('-'):y.find('-')+4] + '.' + y[y.find('-')+4:y.find('\n')])
data.close()

g_l = Graph_l(len(cityname)) #initializatoin of list graph


#       Equation that converts lat-long to distance in miles        #
adjacencyMat = [[0 for i in range(len(latitude))] for j in range(len(longitude))] # creates an adjacency matrix
adjacencyList = defaultdict(list) # creates an adjacency list
for i in range(0, len(latitude)):
    for j in range(0, len(longitude)):
        p = 0.017453292519943295     #Pi/180
        a = 0.5 - math.cos((float(latitude[j]) - float(latitude[i])) * p)/2 + math.cos(float(latitude[i]) * p) * math.cos(float(latitude[j])* p) * (1 - math.cos((float(longitude[j]) - float(longitude[i])) * p)) / 2
        d= 7922 * math.asin(math.sqrt(a))
        if d <= 30: #if distance is less than 30 miles it has a direct connection
            adjacencyMat[i][j] = d #matrix inputing
            newNode = [cityname[j], d] #list inputint
            adjacencyList[i].insert(0, newNode)
            g_l.addEdge(i, j, d)

f = open("adjList.txt",'w')
for i in adjacencyList: #makes a that contains adj list of starting graph
    f.write('#{}: {}\n\n'.format(cityname[i], adjacencyList[i]))
f.close()   
#print(cityname)
#print(population)
#print(latitude)
#print(longitude) 


adjacencyListOut = defaultdict(list)

totaltime = 0

g = Graph_Matrix(len(cityname))
g.graph = adjacencyMat
timestart = time.time()
g.primMST() # call to matrix version of prims
totaltime = totaltime + (time.time() - timestart)
print(totaltime)
f = open("prims_mat_out.txt",'w')
f.write(str(adjacencyMat))
f.close()
timestart = time.time()
g_l.PrimMST() #call to list version of prims
totaltime = totaltime + (time.time() - timestart)
print(totaltime)
f = open("prims_list_out.txt",'w')
for i in range(len(adjacencyListOut)):
    f.write('#{}: {}\n'.format(cityname[i], adjacencyListOut[i]))
f.close()
