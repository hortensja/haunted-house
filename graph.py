from math import sqrt


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, v):
        self.vertices[v.name] = v

    def add_edge(self, e):
        self.edges[e.vertices] = e

    def get_vertex(self, name):
        return self.vertices[name]

    def get_edge(self, v):
        return self.edges[v]

    def get_neighbrohood(self, v: "Vertex"):
        dist = v.dist+1
        indices = filter(lambda t: t[0]==v.name, self.edges.keys())
        map(lambda e: (self.get_edge(e)).set_dist(dist), indices)
        return map(lambda t: self.get_vertex(t[1]), indices)

    def bfs(self, root: "Vertex"):
        root.set_colour("pink")
        root.set_dist(0)
        Q = [root]
        while Q:
            u = Q.pop()
            for v in self.get_neighbrohood(u):
                if v.colour is None:
                    new_dist = u.dist+1
                    v.set_colour("pink")
                    v.set_dist(new_dist)
                    v.set_parent(u)
                    e = self.get_edge((u.name, v.name))
                    e.set_length_bfs(new_dist)
                    Q.append(v)
            u.set_colour("red")
        return self



    def __str__(self):
        return '\nVertices:\n' + "\n".join(map(str, self.vertices.values())) + '\n\nEdges:\n' + "\n".join(map(str, self.edges.values()))



class Vertex:
    def __init__(self, name):
        self.name = name
        self.colour = None
        self.dist = float("inf")
        self.parent = None

    def set_colour(self, colour):
        self.colour = colour

    def set_dist(self, dist):
        self.dist = dist

    def set_parent(self, parent: "Vertex"):
        self.parent = parent

    def calculate_dist(self, other):
        x = (self.name%4)-(other.name%4)
        y = (self.name//4)-(other.name//4)
        return sqrt(x**2+y**2)

    def __str__(self):
        p = None
        if self.parent is not None:
            p = self.parent.name
        return '({}, col: {}, dist: {}, parent: {})'.format(self.name, self.colour, self.dist, p)


class Edge:
    def __init__(self, v: tuple):
        self.vertices = v
        self.length_bfs = None

    def set_length_bfs(self, l):
        self.length_bfs = l

    def __eq__(self, other):
        return (self.vertices == other.vertices)

    def __str__(self):
        return '{}--{}, bfs: {}'.format(self.vertices[0], self.vertices[1], self.length_bfs)
