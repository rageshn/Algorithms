"""

Problem: Single source shortest path
--------
Assumptions: Directed/Undirected Graph & each edge has non-negative weights
------------

Algorithm:
-----------

Dijkstra(Graph G):
    Create Min-Heap[# of vertices]
    Each Node of Min-Heap contains Vertex with distance value of vertex.
    Initialize Min-Heap with source vertex as ROOT, and distance is set to 0.
    Assign distance to other vertices as INFINITY.
    While(Min-Heap is not empty):
        Extract Vertex 'U' which has min distance from Min-Heap.
        For each Vertex V in G[U]:
            if V is in Min-Heap:
                if(dist > Weight of U-V + dist(U))
                    update Dist(V)


Time Complexity:
-----------------
Naive implementation: theta(V*E)  --> theta(# of vertices X # of edges)
Heap implementation: O((E + V)*log(V)) or O(E*log(V))

"""

import heapq

raw = open("/home/ragesh/PycharmProjects/Algorithms/resources/directedweightedgraph", "r")

graph = {}

for line in raw:
    value = line.split()
    vertex = int(value[0])
    graph[vertex] = []
    for val in value[1:]:
        edge, weight = val.split(',')
        graph[vertex].append([int(edge), int(weight)])


def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()

    while(heap):
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue

        visited.add(u)
        if u == end:
            return cost

        for v, c in graph[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))

    return -1


shortDist = dijkstra(graph, 1, 200)

print(shortDist)