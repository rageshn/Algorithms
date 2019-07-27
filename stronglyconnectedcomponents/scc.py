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

import sys
sys.setrecursionlimit(300000)
# dfs implementation
# 0 unvisited
# 1 visited
# 2 explored

# globals
visited = {}
finish = {}
leader = {}

# number of nodes
N = 875714
# Graph
G = {}
# Transpose of graph
GT = {}


# Initializes the values
def init():
    for index in range(1, N + 1):
        visited[index] = 0
        finish[index] = 0
        leader[index] = 0


# Initializes every index with an array to hold the out links
for i in range(1, N + 1):
    G[i] = []
    GT[i] = []


# Reads the input file and set the graph and transpose graph values
f = open("/home/ragesh/PycharmProjects/Algorithms/resources/scc","r")
for line in f.readlines():
    value = line.split()
    x = int(value[0])
    y = int(value[1])
    G[x].append(y)
    GT[y].append(x)


# For all the nodes, if unvisited, calls dfs with graph for every node
def dfs_loop(G):
    # number of nodes processed so far
    global t
    # Current source vertex from which DFS was initiated
    global s
    t = 0
    s = 0
    i = N
    while i > 0:
        if visited[i] == 0:
            s = i
            dfs(G, i)
        i -= 1


# For every out links in a node. if unvisited, recursively calls dfs.
def dfs(G, i):
    global t
    visited[i] = 1
    leader[i] = s
    for j in G[i]:
        if visited[j] == 0:
            dfs(G, j)
    t += 1
    finish[i] = t


init()
dfs_loop(GT)


newgraph = {}
for i in range(1, N + 1):
    temp = []
    for x in G[i]:
        temp.append(finish[x])
    newgraph[finish[i]] = temp


init()
dfs_loop(newgraph)


a_list = sorted(leader.values())
stat = []
pre = 0
for i in range(0, N - 1):
    if a_list[i] != a_list[i+1]:
        stat.append(i+1-pre)
        pre = i+1
stat.append(N-pre)
final_answer = sorted(stat)
final_answer.reverse()
print(final_answer[0:5])
