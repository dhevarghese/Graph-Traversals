import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np
from networkx.exception import NetworkXError
from vertex import Vertex

class Graph():
    def __init__(self):
        self.verticies = {}
        #self.G = nx.Graph() #Used for visualisation
        self.G = nx.DiGraph() #Used for visualisation of directed graph
        self.colorMap = []

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex
        self.G.add_node(vertex.key)
    
    def delete_vertex(self, vertex):
        try:
            self.G.remove_node(vertex.key)
            return self.verticies.pop(vertex.key)
        except KeyError or NetworkXError:
            return None

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.G.add_edge(from_key, to_key)
        self.verticies[from_key].add_neighbor(self.verticies[to_key], weight)
        

    def delete_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            return None
        if to_key not in self.verticies:
            return None
        try:
            self.G.remove_edge(from_key, to_key)
        except NetworkXError:
            return None
        return self.verticies[from_key].delete_neighbor(self.verticies[to_key])


    def get_vertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())

    #currVertex is a vertex key
    def DFSF(self,currVertex):
        if(currVertex not in self.verticies.keys()):
          return None
        visited = {x: False for x in self.verticies} 
        ordVisited = []
        stack = []
        stack.append(currVertex) 
        while (len(stack)): 
            currVertex = stack.pop()
            if (not visited[currVertex]): 
                print(currVertex,end=' ')
                ordVisited.append(currVertex)
                visited[currVertex] = True
            for neighbor in self.verticies[currVertex]:
                if (not visited[neighbor.key]): 
                    stack.append(neighbor.key)
        return ordVisited

    def BFSF(self,currVertex):
        visited = {x: False for x in self.verticies} 
        ordVisited = []     # Mark all the vertices as not visited
        queue = []                                        # Create a queue for BFS
        queue.append(currVertex)
        #node_pos = nx.spring_layout(self.G, seed = 75)    # Mark the source node as 
        #self.visualiseVisited(visited, node_pos)

        visited[currVertex] = True                        # visited and enqueue it
        print(currVertex)
        ordVisited.append(currVertex)
        #self.visualiseVisited(visited, node_pos)


        while queue:
            currVertex = queue.pop(0)                       # Dequeue a vertex from 
            #print (currVertex, end = " ")
                                                            # queue and print it
            for i in self.verticies[currVertex]:            # Get all adjacent vertices of the
                if visited[i.key] == False:                 # dequeued vertex s. If a adjacent
                    queue.append(i.key)                     # has not been visited, then mark it
                    visited[i.key] = True
                    print(i.key, end = " ")
                    ordVisited.append(i.key)
                    #self.visualiseVisited(visited, node_pos)# visited and enqueue it
        return ordVisited

    #currVertex is a vertex key
    def DFS(self,currVertex):
        if(currVertex not in self.verticies.keys()):
          return None
        node_pos = nx.spring_layout(self.G, seed = 75)
        visited = {x: False for x in self.verticies} 
        stack = []
        stack.append(currVertex) 
        while (len(stack)): 
            currVertex = stack.pop()
            if (not visited[currVertex]): 
                print(currVertex,end=' ')
                #print(self.verticies[currVertex])
                visited[currVertex] = True
                self.visualiseVisited(visited, node_pos)
            for neighbor in self.verticies[currVertex]:
                if (not visited[neighbor.key]): 
                    stack.append(neighbor.key)

    def visualiseVisited(self, visited, nodePos):
        color_map = []
        for node in visited:
            if visited[node] == False:
                color_map.append('r')
            else: 
                color_map.append('green')      
        nx.draw_networkx(self.G, node_color=color_map, pos = nodePos, with_labels=True)
        plt.show() 

    def BFS(self,currVertex):
        visited = {x: False for x in self.verticies}      # Mark all the vertices as not visited
        queue = []                                        # Create a queue for BFS
        queue.append(currVertex)
        node_pos = nx.spring_layout(self.G, seed = 75)    # Mark the source node as 
        self.visualiseVisited(visited, node_pos)
        
        visited[currVertex] = True                        # visited and enqueue it
        print(currVertex)                     
        self.visualiseVisited(visited, node_pos)
       

        while queue:
            currVertex = queue.pop(0)                       # Dequeue a vertex from 
            #print (currVertex, end = " ")
                                                            # queue and print it
            for i in self.verticies[currVertex]:            # Get all adjacent vertices of the
                if visited[i.key] == False:                 # dequeued vertex s. If a adjacent
                    queue.append(i.key)                     # has not been visited, then mark it
                    visited[i.key] = True
                    print(i.key, end = " ")
                    self.visualiseVisited(visited, node_pos)# visited and enqueue it

    
    def visualize(self):
        try:
            my_pos = nx.spring_layout(self.G, seed = 100)
            nx.draw_networkx(self.G, pos = my_pos)
            plt.show()
        except AttributeError:
            return None

    def length(self):
      return self.size

    def adjmat(self):
      
      self.adjMatrix=[]
      for i in range(self.size):

            self.adjMatrix.append([0 for i in range(self.size)])
      
      for i in self.verticies.keys():
        
        s=self.get_vertex(i).__str__()
        for j in self.verticies.keys():
          
          if str(j) in self.get_vertex(i).__str__() and str(j)!=s[0]:
            if max(i,j)>=len(self.adjMatrix):
              self.adjMatrix=self.expand(self.adjMatrix,max(i,j)+1)
            self.adjMatrix[i][j]=1

      return self.adjMatrix
        
     
    
    def adjlist(self):
      alist=[]
      for i in self.verticies.keys():
        s=""  
        #s+="Adjacency list for vertex "
        s+=str(i)
        s+=": Head ->"
        print(self.get_vertex(i))
        for j in self.get_vertex(i).get_neighbor():
          
          s+=str(j.key)
          s+=" -> "
        s+="None" 
        alist.append(s)
      return alist
        
            
      
    def expand(self,mat,n):
      nm=[[0]*n for i in range(n)]
      for i in range(len(mat)):
        for j in range(len(mat[i])):
          nm[i][j]=mat[i][j]
      return nm

    def clearVertices(self):
        self.verticies.clear()
        self.size=0
        
        '''
        for i in self.verticies.keys():
            self.delete_vertex(Vertex(i))
        '''
        print(self.verticies)