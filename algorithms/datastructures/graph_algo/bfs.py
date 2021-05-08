from collections import defaultdict

class Graph:
    def __init__(self):
        self.gdidct = defaultdict(list)
    
    def addEdge(self,u,v):
        self.gdidct[u].append(v)


    def BFS(self,s):
        visited = set()
        queue = []

        queue.append(s)
        visited.add(s)

        while queue:
            v = queue.pop(0)
            print(v)

            for i in self.gdidct[v]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)