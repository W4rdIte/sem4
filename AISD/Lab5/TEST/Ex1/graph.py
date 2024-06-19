import random
import numpy as np


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_matrix = np.zeros((size, size))
        self.edges = []

    @staticmethod
    def generate_random_complete_graph(size):
        graph = Graph(size)
        for i in range(size):
            for j in range(i + 1, size):
                graph.add_random_weighted_edge(i, j)
        return graph

    def add_weighted_edge(self, node1, node2, weight):
        self.edges.append(Edge(node1, node2, weight))
        self.adjacency_matrix[node1][node2] = weight
        self.adjacency_matrix[node2][node1] = weight

    def add_random_weighted_edge(self, node1, node2):
        self.add_weighted_edge(node1, node2, self.generate_random_weight())

    def generate_random_weight(self):
        return random.uniform(0.0, 1.0)

    def generate_kruskals_minimum_spanning_tree(self):
        parents = [i for i in range(self.size)]
        ranks = [0] * self.size

        edges = sorted(self.edges, key=lambda edge: edge.weight)
        mst = Graph(self.size)

        for edge in edges:
            if self.find(edge.node1, parents) != self.find(edge.node2, parents):
                mst.add_weighted_edge(edge.node1, edge.node2, edge.weight)
                self.unite(edge.node1, edge.node2, parents, ranks)

        return mst

    def generate_prims_minimum_spanning_tree(self):
        visited = [False] * self.size
        cost = [float("inf")] * self.size
        previous = [-1] * self.size

        cost[0] = 0

        for _ in range(self.size - 1):
            min_node = self.find_min_node(cost, visited)
            visited[min_node] = True

            for neighbor_node in range(self.size):
                if (
                    not visited[neighbor_node]
                    and self.adjacency_matrix[min_node][neighbor_node] != 0
                    and self.adjacency_matrix[min_node][neighbor_node]
                    < cost[neighbor_node]
                ):
                    cost[neighbor_node] = self.adjacency_matrix[min_node][neighbor_node]
                    previous[neighbor_node] = min_node

        mst = Graph(self.size)
        for i in range(1, self.size):
            mst.add_weighted_edge(previous[i], i, self.adjacency_matrix[i][previous[i]])

        return mst

    def find_min_node(self, cost, visited):
        min_value = float("inf")
        min_index = -1

        for node in range(self.size):
            if not visited[node] and cost[node] < min_value:
                min_value = cost[node]
                min_index = node

        return min_index

    def find(self, node, parents):
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]

    def unite(self, node1, node2, parents, ranks):
        root1 = self.find(node1, parents)
        root2 = self.find(node2, parents)

        if root1 != root2:
            if ranks[root1] < ranks[root2]:
                parents[root1] = root2
            elif ranks[root1] > ranks[root2]:
                parents[root2] = root1
            else:
                parents[root2] = root1
                ranks[root1] += 1

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def get_edges(self):
        return self.edges
