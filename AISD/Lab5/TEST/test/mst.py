class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = {i: [] for i in range(size)}

    def add_weighted_edge(self, node1, node2, weight):
        self.adjacency_list[node1].append((node2, weight))
        self.adjacency_list[node2].append((node1, weight))

    def find(self, node, parents):
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]

    def unite(self, node1, node2, parents, ranks):
        root1 = self.find(node1, parents)
        root2 = self.find(node2, parents)
        if root1 != root2:
            if ranks[root1] > ranks[root2]:
                parents[root2] = root1
            elif ranks[root1] < ranks[root2]:
                parents[root1] = root2
            else:
                parents[root2] = root1
                ranks[root1] += 1

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


def dfs_order(node, graph, visited, order):
    visited[node] = True
    order.append(node)
    for neighbor, _ in graph.adjacency_list[node]:
        if not visited[neighbor]:
            dfs_order(neighbor, graph, visited, order)


def compute_min_rounds(graph, root):
    visited = [False] * graph.size
    order = []
    dfs_order(root, graph, visited, order)
    order.reverse()

    max_depth = 0
    depth = [0] * graph.size

    def dfs(node, current_depth):
        nonlocal max_depth
        depth[node] = current_depth
        max_depth = max(max_depth, current_depth)
        for neighbor, _ in graph.adjacency_list[node]:
            if depth[neighbor] == 0:  # Unvisited
                dfs(neighbor, current_depth + 1)

    dfs(root, 0)
    return max_depth


def find_min_node(self, cost, visited):
    min_value = float("inf")
    min_index = -1

    for node in range(self.size):
        if not visited[node] and cost[node] < min_value:
            min_value = cost[node]
            min_index = node

    return min_index
