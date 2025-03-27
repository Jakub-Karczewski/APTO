import copy
import graphviz as gv
import heapq

Gr = gv.Graph(format='png',
              filename='graph.gv')


# engine='fdp'

class Edge:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.visit = False


def get_neighbours_list(E, n):
    neigh = [[] for _ in range(n)]
    for (l, r) in E:
        x = Edge(l, r)
        neigh[l].append(x)
        neigh[r].append(x)
    return neigh


V = 8
edges = [(1, 2), (0, 2), (2, 3), (3, 4), (3, 5), (5, 6), (5, 7)]
e = len(edges)
Graph = get_neighbours_list(edges, V)
for i in range(V):
    Gr.node(str(i), str(i))
for i in range(e):
    Gr.edge(str(edges[i][0]), str(edges[i][1]))


# Gr.render(".\\Graph", view=True)

def approx_2():
    G = copy.deepcopy(Graph)
    sol = 0
    for i in range(V):
        for j in range(len(G[i])):
            edge = G[i][j]
            if not edge.visit:
                print((edge.l, edge.r))
                sol += 2
                for k in range(len(G[edge.l])):
                    G[edge.l][k].visit = True
                for k in range(len(G[edge.r])):
                    G[edge.r][k].visit = True
    return sol


def approx_logn():
    my_heap = []
    for i in range(V):
        heapq.heappush(my_heap, (-len(Graph[i]), i))
    act_e = e
    G = copy.deepcopy(Graph)
    while act_e > 0:
        maxi = heapq.heappop(my_heap)
        print((-maxi[0], maxi[1]))
        if not len(my_heap):
            break


print(approx_2())
approx_logn()
