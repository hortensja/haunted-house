class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, v):
        self.vertices.append(v)

    def add_edge(self, e):
        self.edges.append(e)

    def get_vertex(self, name):
        return None


    def __str__(self):
        return 'Vertices: ',self.vertices, '\nEdges: ', self.edges



class Vertex:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return (self.name == other.name)


class Edge:
    def __init__(self, v):
        self.vertices = v
        self.length = None

    def set_length(self, l):
        self.length = l