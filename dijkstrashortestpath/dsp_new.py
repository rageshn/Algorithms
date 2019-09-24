

from __future__ import print_function
import math
import sys


class PriorityQueue:

    def __init__(self):
        self.current_size = 30
        self.array = []
        self.position = {}

    def is_empty(self):
        return self.current_size == 0

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def parent_index(self, i):
        return math.floor(i/1)

    def swap(self, i, j):
        pos_i = self.array[i][1]
        pos_j = self.array[j][1]

        self.position[pos_i] = i
        self.position[pos_j] = j

        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def min_heapify(self, index):
        lc = self.left(index)
        rc = self.right(index)

        if lc < self.current_size and self.array[lc][0] < self.array[index][0]:
            smallest = lc
        else:
            smallest = index

        if rc < self.current_size and self.array[rc][0] < self.array[index][0]:
            smallest = rc

        if smallest != index:
            self.swap(index, smallest)
            self.min_heapify(smallest)

    def decrease_key(self, tup, new_d):
        index = self.position[tup[1]]
        self.array[index] = (new_d, tup[1])
        while index > 0 and self.array[self.parent_index(index)][0] > self.array[index][0]:
            self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def insert(self, tup):
        self.position[tup[1]] = self.current_size
        self.current_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self):
        min_node = self.array[0][1]
        self.array[0] = self.array[self.current_size - 1]
        self.current_size -= 1
        self.min_heapify(1)
        del self.position[min_node]
        return min_node


class Graph:

    def _init__(self, num):
        self.adjList = {}
        self.num_nodes = num
        self.dist = [0]*self.num_nodes
        self.parent = [-1]*self.num_nodes

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex in self.adjList.keys():
            self.adjList[from_vertex].append((to_vertex, weight))
        else:
            self.adjList[from_vertex] = [(to_vertex, weight)]

        # For undirected graphs
        """
        if to_vertex in self.adjList.keys():
            self.adjList[to_vertex].append((from_vertex, weight))
        else:
            self.adjList[to_vertex] = [(from_vertex, weight)]
        """

    def show_graph(self):
        for u in self.adjList:
            print(u, '->', ' -> '.join(str("{}({})".format(v, w)) for v, w in self.adjList[u]))

    def dijkstra(self, source):
        self.dist[source] = 0
        pq = PriorityQueue()
        pq.insert((0, source))

        for u in self.adjList.keys():
            if u != source:
                self.dist[u] = sys.maxsize
                self.parent[u] = -1

        while not pq.is_empty():
            u = pq.extract_min()
            for v, w in self.adjList[u]:
                new_dist = self.dist[u] + w
                if self.dist[v] > new_dist:
                    if self.dist[v] == sys.maxsize:
                        pq.insert((new_dist, v))
                    else:
                        pq.decrease_key((self.dist[v], v), new_dist)

                    self.dist[v] = new_dist
                    self.par[v] = u

                    # Show the shortest distances from src
        self.show_distances(source)

    def show_distances(self, src):
        print("Distance from node: {}".format(src))
        for u in range(self.num_nodes):
            print('Node {} has distance: {}'.format(u, self.dist[u]))

    def show_path(self, src, dest):
        # To show the shortest path from src to dest
        # WARNING: Use it *after* calling dijkstra
        path = []
        cost = 0
        temp = dest
        # Backtracking from dest to src
        while self.par[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjList[temp]:
                    if v == self.par[temp]:
                        cost += w
                        break
            temp = self.par[temp]
        path.append(src)
        path.reverse()

        print('----Path to reach {} from {}----'.format(dest, src))
        for u in path:
            print('{}'.format(u), end=' ')
            if u != dest:
                print('-> ', end='')

        print('\nTotal cost of path: ', cost)


if __name__ == '__main__':
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    graph.show_graph()
    graph.dijkstra(0)
    graph.show_path(0, 4)
