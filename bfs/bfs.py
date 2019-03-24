"""

Algorithm:
-----------

BFS(Graph G, StartVertex S):
    [All nodes initially unexplored]
    Mark S as explored
    Let Q = Queue initialized with S
    while Q is not empty:
        V = pop the element from Q
        For each edges (V, W):
            if W is unexplored:
                Mark W as explored
                Add W to Q

Time Complexity: O(V+E)

"""

from queue import Queue

raw = open("/home/ragesh/PycharmProjects/Algorithms/resources/graph", "r")

graph = {}

for line in raw:
    values = line.split()
    node = int(values[0])
    edges = list(map(int, values[1:]))
    graph[node] = edges


def bfs(G, startNode):
    Q = Queue(len(G.values()))
    Q.put(startNode)
    explored = []
    explored.append(startNode)
    while not Q.empty():
        V = Q.get()
        for edge in G[V]:
            if edge not in explored:
                explored.append(edge)
                Q.put(edge)

    print("Explored order: ", explored)


bfs(graph, startNode=5)
