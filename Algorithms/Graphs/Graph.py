##Graph class
#This is adjacency list

class Graph:
    def __init__(self, V):
        #array
        self.vertices = [None] * len(V)
        for i in range(V):
            self.vertices[i] = Vertex(V[i])
        def __str__(self):
            return_string = ""
            for vertex in self.vertices:
                return_string = return_string + "," + str(vertex)
            return return_string
class Vertex:
    def __init__(self):
        self.id = id
        #list
        self.edges = []
    def __str__(self):
        return_string = str(self.id) 
        return return_string

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

#Create a graph with 5 vertices

if __name__ == "__main__":
    vertices = [0,1,2,3,4]
    my_graph = Graph(V=vertices)
                     
