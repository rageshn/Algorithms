"""

Also known as Karger Minimum cut problem.

Goal: In an undirected graph G = (V, E), compute a cut with fewest number of crossing edges.

Algorithm:
-----------
While there are more than 2 nodes:
    Pick remaining edges (U, V) uniformly at random.
    Merge (or contract) U and V into a single node.
    remove self-loops
return the cut represented by final 2 vertices.


Time complexity: Polynomial over 'n' and 'm'. Nearly Omega(n^2 * m)

"""

import random

raw = open("resources/graph", "r")

graph = {}

for line in raw:
    node = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))
    graph[node] = edges
raw.close()

def karger(graph):
    while len(graph) > 2:
        # For final step, when only two vertices are left in the graph
        keys = list(graph.keys())
        start = random.choice(keys)
        finish = random.choice(graph[start])
        # Randomly choosing the edge that will be collapsed to the start node.

        # Adding edges from the absorbed node
        for edge in graph[finish]:
            if edge != start:  # This prevents to have self loop
                graph[start].append(edge)  # This will add the edges to the collapsed node to the start.

        # Deleting the references to the absorbed node and changing them to the source node
        for edge in graph[finish]:
            graph[edge].remove(finish)
            if edge != start:
                graph[edge].append(start)
        del graph[finish]
    print(graph)
    for i in graph:
        print(len(graph[i]))

karger(graph)


