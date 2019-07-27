"""

Algorithm (Kosraju's Two-Pass Algorithm):
------------------------------------------

High level:
------------
G = Directed graph
G_rev = G with all edges reversed
run DFS_Loop on G_rev
    --> Computes ordering of nodes
    --> Set f(V) = Finishing time of each vertex
run DFS_Loop on G
    --> Processes nodes in the decreasing order of the finishing times
    --> Discovers the SCC one-by-one
    --> SCCs = nodes with the same leader


DFS_Loop(Graph G):
    Initiate t = 0 (Global Variable - Count the number of nodes explored at a moment, for computing finishing times) -> accessed in first pass
    Initiate S = NULL (Source Vertex from which DFS was initiated) -> accessed in second pass
    Assume nodes labelled as 1 to N
    For V = N to 1:
        if V is unexplored:
            S = V
            DFS(G, V)


DFS(Graph G, StartVertex V):
    [All nodes initially unexplored]
    Mark V as explored
    Set Leader(V) = S
    For every edge (V,W):
        if W is unexplored:
            DFS(G,W)

    t = t++
    Set f(V) = t

Time Complexity: O(V+E)

"""

raw = open("/home/ragesh/PycharmProjects/Algorithms/resources/scc", "r")

graph = {}
graph_reversed = {}
explored = []
leader = {}
finishing_time = {}

vertices = set()  # 875714

# To get all the vertices list
for line in raw:
    values = line.split()
    from_node = int(values[0])
    vertices.add(from_node)
    to_node = int(values[1])
    vertices.add(to_node)

# Initiate graphs
for vertex in vertices:
    graph[vertex] = []
    graph_reversed[vertex] = []
    finishing_time[vertex] = 0
    leader[vertex] = 0


# Build the graph and graph_reversed
for line in raw:
    values = line.split()
    x = int(values[0])
    y = int(values[1])
    graph[x].append(y)
    graph_reversed[y].append(x)


def dfs(graph, startnode, explored):
    global t
    explored.append(startnode)
    leader[startnode] = s
    for edge in graph[startnode]:
        if edge not in explored:
            dfs(graph, edge, explored)

    t = t+1
    finishing_time[startnode] = t


def dfs_loop(graph):
    global t
    global s
    t = 0
    s = 0
    vertices_reversed = sorted(vertices, reverse=True)
    for node in vertices_reversed:
        if node not in explored:
            s = node
            dfs(graph, node, explored)


def graph_ft(graph, vertices):
    newgraph = {}
    for node in vertices:
        temp = []
        for x in graph[node]:
            temp.append(finishing_time[x])
        newgraph[finishing_time[node]] = temp
    return newgraph


dfs_loop(graph_reversed)
#newgraph = graph_ft(graph, vertices)

#explored = []
#finishing_time = {}
#leader = {}
#dfs_loop(newgraph)


print(finishing_time)