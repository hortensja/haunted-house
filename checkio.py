from graph import Graph, Vertex, Edge

DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}
BLOCKED = (("N", "W"), ("N",), ("N",), ("N", "E"), ("W"), (), (), ("E",), ("W"), (), (), ("E",), ("W", "S"), ("S",), ("S",), ("S", "E"))
EXIT = "N"

def checkio(house, stephan, ghost):


    graph = graphize_house(house)
    #print(graph)

    print(graph.bfs(graph.get_vertex(stephan-1)))

    return "N" or "S" or "W" or "E"



def graphize_house(house):
    graph = Graph()
    for i in range(16):
        graph.add_vertex(Vertex(i))
    for no, h in enumerate(house):
        open = filter(lambda x: x not in h and x not in BLOCKED[no], DIRS)
        for o in open:
            edge = Edge((no, no+DIRS.get(o)))
            graph.add_edge(edge)
    return graph

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from random import choice

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction]
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    checkio(
        ["", "S", "S", "",
         "E", "NW", "NS", "",
         "E", "WS", "NS", "",
         "", "N", "N", ""],
        16, 1)
    # checkio(
    #     ["", "", "", "",
    #      "E", "ESW", "ESW", "W",
    #      "E", "ENW", "ENW", "W",
    #      "", "", "", ""],
    #     11, 6)


    # assert check_solution(checkio,
    #                       ["", "S", "S", "",
    #                        "E", "NW", "NS", "",
    #                        "E", "WS", "NS", "",
    #                        "", "N", "N", ""]), "1st example"
    # assert check_solution(checkio,
    #                       ["", "", "", "",
    #                        "E", "ESW", "ESW", "W",
    #                        "E", "ENW", "ENW", "W",
    #                        "", "", "", ""]), "2nd example"
