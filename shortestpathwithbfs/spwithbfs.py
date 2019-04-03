"""

Algorithm:
-----------

BFS(Graph G, StartVertex S):
    [All nodes initially unexplored]
    Initiate dist(V) = 0, if V == S
             dist(V) = INFINITY, if V != S
    Mark S as explored
    Let Q = Queue initialized with S
    while Q is not empty:
        V = pop the element from Q
        For each edges (V, W):
            if W is unexplored:
                Set dist(W) = dist(V) + 1
                Mark W as explored
                Add W to Q

Time Complexity: O(V+E)

"""

from queue import Queue

raw = open("/home/ragesh/PycharmProjects/Algorithms/resources/graph", "r")

graph = {}
distance = {}

for line in raw:
    values = line.split()
    node = int(values[0])
    edges = list(map(int, values[1:]))
    graph[node] = edges


def bfs(G, startNode):
    Q = Queue(len(G.values()))
    Q.put(startNode)
    distance[startNode] = 0
    explored = []
    explored.append(startNode)
    while not Q.empty():
        V = Q.get()
        for edge in G[V]:
            if edge not in explored:
                distance[edge] = distance[V] + 1
                explored.append(edge)
                Q.put(edge)

    print("Explored order: ", explored)
    sorted_dist = sorted(distance.items(), key=lambda kv: kv[1])
    print("Sorted based on distance: ", sorted_dist)


bfs(graph, startNode=10)
