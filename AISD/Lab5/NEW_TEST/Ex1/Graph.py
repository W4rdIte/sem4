import random
import numpy as np
from queue import Queue
from typing import List, Tuple


class Edge:
    def __init__(self, node1: int, node2: int, weight: float):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


class Graph:
    UNCONNECTED_WEIGHT = -1

    def __init__(self, size: int):
        self.size = size
        self.adjacency_matrix = np.full(
            (size, size), self.UNCONNECTED_WEIGHT, dtype=float
        )
        self.edges = []

    @staticmethod
    def generate_random_complete_graph(size: int):
        graph = Graph(size)
        for i in range(size):
            for j in range(i + 1, size):
                graph.add_random_weighted_edge(i, j)
        return graph

    def add_weighted_edge(self, node1: int, node2: int, weight: float):
        self.edges.append(Edge(node1, node2, weight))
        self.adjacency_matrix[node1][node2] = weight
        self.adjacency_matrix[node2][node1] = weight

    def add_random_weighted_edge(self, node1: int, node2: int):
        self.add_weighted_edge(node1, node2, self.generate_random_weight())

    def generate_random_weight(self) -> float:
        return random.uniform(0.0, 1.0)

    def generate_kruskals_minimum_spanning_tree(self):
        previous = list(range(self.size))
        ranks = [0] * self.size

        edges = sorted(self.edges, key=lambda e: e.weight)
        minimum_spanning_tree = Graph(self.size)

        for edge in edges:
            if self.find(edge.node1, previous) != self.find(edge.node2, previous):
                minimum_spanning_tree.add_weighted_edge(
                    edge.node1, edge.node2, edge.weight
                )
                self.unite(edge.node1, edge.node2, previous, ranks)

        return minimum_spanning_tree

    def find(self, node: int, parents: List[int]) -> int:
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]

    def unite(self, node1: int, node2: int, parents: List[int], ranks: List[int]):
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

    def generate_prims_minimum_spanning_tree(self):
        visited = [False] * self.size
        cost = [float("inf")] * self.size
        previous = [-1] * self.size

        cost[0] = 0

        for _ in range(self.size - 1):
            min_node = self.find_min_node(cost, visited)
            visited[min_node] = True

            for neighbor in range(self.size):
                if (
                    not visited[neighbor]
                    and self.adjacency_matrix[min_node][neighbor]
                    != self.UNCONNECTED_WEIGHT
                    and self.adjacency_matrix[min_node][neighbor] < cost[neighbor]
                ):
                    cost[neighbor] = self.adjacency_matrix[min_node][neighbor]
                    previous[neighbor] = min_node

        minimum_spanning_tree = Graph(self.size)
        for i in range(1, self.size):
            minimum_spanning_tree.add_weighted_edge(
                previous[i], i, self.adjacency_matrix[i][previous[i]]
            )

        return minimum_spanning_tree

    def find_min_node(self, cost: List[float], visited: List[bool]) -> int:
        min_value = float("inf")
        min_index = -1

        for node in range(self.size):
            if not visited[node] and cost[node] < min_value:
                min_value = cost[node]
                min_index = node

        return min_index

    def get_adjacency_matrix(self) -> np.ndarray:
        return self.adjacency_matrix

    def get_edges(self) -> List[Edge]:
        return self.edges

    def find_shortest_info_spread_order(
        self, start_node: int
    ) -> Tuple[List[List[int]], List[int]]:
        children_lists = self.create_children_lists(start_node)
        order = [[] for _ in range(self.size)]
        rounds_left = [0] * self.size

        self._find_shortest_info_spread_order(
            start_node, children_lists, order, rounds_left
        )

        return order, rounds_left

    def create_children_lists(self, start_node: int) -> List[List[int]]:
        children_lists = [[] for _ in range(self.size)]
        visited = [False] * self.size
        nodes_to_visit = Queue()

        nodes_to_visit.put(start_node)
        visited[start_node] = True

        while not nodes_to_visit.empty():
            current_node = nodes_to_visit.get()

            for neighbor in range(self.size):
                if (
                    not visited[neighbor]
                    and self.adjacency_matrix[current_node][neighbor]
                    != self.UNCONNECTED_WEIGHT
                ):
                    children_lists[current_node].append(neighbor)
                    nodes_to_visit.put(neighbor)
                    visited[neighbor] = True

        return children_lists

    def _find_shortest_info_spread_order(
        self,
        start_node: int,
        children_lists: List[List[int]],
        order: List[List[int]],
        rounds_left: List[int],
    ):
        if self.is_leaf(start_node, children_lists):
            return

        current_node_children = children_lists[start_node]

        for child in current_node_children:
            self._find_shortest_info_spread_order(
                child, children_lists, order, rounds_left
            )

        for child in current_node_children:
            order[start_node].append(child)

        order[start_node].sort(key=lambda x: rounds_left[x], reverse=True)
        rounds_left[start_node] = rounds_left[order[start_node][0]] + 1

        for i in range(1, len(order[start_node])):
            if rounds_left[start_node] < rounds_left[order[start_node][i]] + i + 1:
                rounds_left[start_node] = rounds_left[order[start_node][i]] + i + 1

    def is_leaf(self, node: int, children_lists: List[List[int]]) -> bool:
        return len(children_lists[node]) == 0
