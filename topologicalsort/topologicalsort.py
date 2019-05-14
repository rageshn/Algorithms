"""

Algorithm:
-----------

DFS(Graph G, startNode S):
    Mark S as explored
    For every edge (S, V):
        if V is unexplored:
            DFS(G, V)
    Add S to Stack


DFS-Loop(Graph G):
    [All nodes initially unexplored]
    Initiate Stack as empty [To keep track of ordering]
    For each vertex V:
        if V is unexplored:
            DFS(G,V)
    return Stack


Time Complexity: O(V+E)
Condition: The graph should be a DAG. If there are any cycles, then there wont be any topological ordering.

"""

raw = open("/home/ragesh/PycharmProjects/Algorithms/resources/dag", "r")

graph = {}

for line in raw:
    values = line.split()
    node = values[0]
    edges = []
    if len(values) > 1:
        edges = list(values[1:])
    graph[node] = edges


def dfs(G, startNode, explored, stack):
    explored.append(startNode)
    for edge in G[startNode]:
        if edge not in explored:
            dfs(G, edge, explored, stack)
    stack.append(startNode)


def topological_sort(graph):
    stack, explored = [], []
    vertices = list(graph.keys())
    for vertex in vertices:
        if vertex not in explored:
            dfs(graph, vertex, explored, stack)

    # Printing the values in proper order (i.e., values are appended at the end)
    print(stack[::-1])


topological_sort(graph)
