from collections import defaultdict

class Graph:
    def __init__(self):
        self.gdict = defaultdict(list)
    
    def addEdge(self,u,v):
        self.gdict[u].append(v)

    def DFSutil(self,v,visited):
        visited.add(v)
        print(v)
        for neighbour in self.gdict[v]:
            if neighbour not in visited:
                self.DFSutil(neighbour,visited)

    def DFS(self,v):
        visited = set()
        # For connected graph
        self.DFSutil(v,visited)

        # For disconnected graph
        # for v in list(self.gdict):
        #     if v not in visited:
        #         self.DFSutil(v,visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)