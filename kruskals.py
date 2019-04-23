from collections import defaultdict
import math
import time
import matplotlib.pyplot as plt 


class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 
          
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    # The main function to construct MST using Kruskal's  
        # algorithm 
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
  
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
  
            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2])
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration 
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            # If including this edge does't cause cycle,  
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([u,v,float(w)])
                self.union(parent, rank, x, y) 
            # Else discard the edge
  
        # print the contents of result[] to display the built MST 
        print( "Following are the edges in the constructed MST")
        f = open("kruskals_output.txt",'w')
        for i in range(len(result)):
            adjacencyList[result[i][0]].insert(0, [cityname[result[i][1]], result[i][2]])
        for i in range(len(cityname)):
            f.write(str('{}: {}\n'.format(cityname[i], adjacencyList[i])))
        f.close()
        #for u,v,weight in result
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            #print("%d -- %d == %d" % (u,v,weight)) 



filearray = [] # array to hold 
cityname = []
population = []
latitude = []
longitude = []
distance = []
R = 3961
    ###     File splitting  ###
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
g = Graph(len(cityname))

#       Equation that converts lat-long to distance in miles        #
adjacencyMat = [[0 for i in range(len(latitude))] for j in range(len(longitude))] # create an adjacency matrix all initialized to 0
adjacencyList = defaultdict(list) #create an adjacency list 
for i in range(0, len(latitude)):
    for j in range(0, len(longitude)):
        p = 0.017453292519943295     #Pi/180
        a = 0.5 - math.cos((float(latitude[j]) - float(latitude[i])) * p)/2 + math.cos(float(latitude[i]) * p) * math.cos(float(latitude[j])* p) * (1 - math.cos((float(longitude[j]) - float(longitude[i])) * p)) / 2
        d= 7922 * math.asin(math.sqrt(a))
        if d <= 30:
            adjacencyMat[i][j] = d
            #newNode = [j, d]
            #adjacencyList[i].insert(0, newNode)
            g.addEdge(i, j, d) # adds an edge given the starting node i, end node j, and distance/weight w
 
#print(g.graph)  
# Driver code
totaltime = 0
timestart = time.time()
g.KruskalMST() 
totaltime = totaltime + (time.time() - timestart)
print(totaltime)

plt.plot(len(cityname),totaltime)
plt.draw()
plt.show()
