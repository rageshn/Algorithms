"""

Algorithm (Recursive):
-----------------------

DFS(Graph G, StartVertex S):
    [All nodes initially unexplored]
    Mark S as explored
    For every edge (S,V):
        if V is unexplored:
            DFS(G,V)



Algorithm (Non-Recursive):
---------------------------

DFS(Graph G, startVertex S):
    [All nodes initially unexplored]
    Mark S as explored
    Let St = Stack initialized with S
    while St is not empty:
        V = pop the element from St
        For each edges (V, W):
            if W is unexplored:
                Mark W as explored
                Add W to St


Time Complexity: O(V+E) --> O(# of nodes reachable from S + # of edges reachable from S)

=> Used in maze problems

"""


raw = open("/home/ragesh/PycharmProjects/Algorithms/resources/graph", "r")

graph = {}

for line in raw:
    values = line.split()
    node = int(values[0])
    edges = list(map(int, values[1:]))
    graph[node] = edges


def dfs_nonrecursive(G, startNode):
    stack, explored = [], []

    explored.append(startNode)
    stack.append(startNode)
    while len(stack) > 0:
        V = stack.pop()
        for edge in G[V]:
            if edge not in explored:
                explored.append(edge)
                stack.append(edge)

    print("Explored order: ", explored)


def dfs_recursive(G, startNode, explored):
    explored.append(startNode)
    for edge in G[startNode]:
        if edge not in explored:
            dfs_recursive(G, edge, explored)
    return explored


dfs_nonrecursive(graph, 5)

explored_order = dfs_recursive(graph, 5, [])
print(explored_order)
