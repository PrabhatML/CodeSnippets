# Graph
class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return (list(self.gdict.keys()))

    def findedges(self):
        edgename = []
        for v in self.gdict:
            for next_v in self.gdict[v]:
                if {v,next_v} not in edgename:
                    edgename.append({v,next_v})
        return edgename

    def addVertex(self,vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def AddEdge(self,edge):
        edge = set(edge)
        (vrtx1,vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
            
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }
g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.findedges())