import random
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = {i: [] for i in range(size)}
        self.edges = []

    def add_weighted_edge(self, node1, node2, weight):
        self.adjacency_list[node1].append((node2, weight))
        self.adjacency_list[node2].append((node1, weight))
        self.edges.append((node1, node2, weight))

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

        edges = sorted(self.edges, key=lambda edge: edge[2])
        mst = Graph(self.size)

        for edge in edges:
            node1, node2, weight = edge
            if self.find(node1, parents) != self.find(node2, parents):
                mst.add_weighted_edge(node1, node2, weight)
                self.unite(node1, node2, parents, ranks)

        return mst

    def generate_prims_minimum_spanning_tree(self):
        visited = [False] * self.size
        cost = [float("inf")] * self.size
        previous = [-1] * self.size

        cost[0] = 0

        for _ in range(self.size):
            min_cost = float("inf")
            min_node = -1
            for node in range(self.size):
                if not visited[node] and cost[node] < min_cost:
                    min_cost = cost[node]
                    min_node = node

            visited[min_node] = True

            for neighbor, weight in self.adjacency_list[min_node]:
                if not visited[neighbor] and weight < cost[neighbor]:
                    cost[neighbor] = weight
                    previous[neighbor] = min_node

        mst = Graph(self.size)
        for i in range(1, self.size):
            if previous[i] != -1:  # Only add edges where a valid parent exists
                # Ensure both nodes are within adjacency list bounds
                if i in self.adjacency_list[previous[i]]:
                    mst.add_weighted_edge(
                        previous[i], i, self.adjacency_list[previous[i]][i]
                    )
                elif previous[i] in self.adjacency_list[i]:
                    mst.add_weighted_edge(
                        previous[i], i, self.adjacency_list[i][previous[i]]
                    )

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


def generate_random_graph(size):
    graph = Graph(size)
    edges = []
    for i in range(size):
        for j in range(i + 1, size):
            if random.random() < 0.5:  # Probability of having an edge
                weight = random.randint(1, 100)  # Random weight
                graph.add_weighted_edge(i, j, weight)

    return graph


def generate_mst_prim(graph):
    mst = graph.generate_prims_minimum_spanning_tree()
    return mst


def generate_mst_kruskal(graph):
    mst = graph.generate_kruskals_minimum_spanning_tree()
    return mst


def experiment(num_graphs, sizes):
    average_rounds_prim = []
    max_rounds_prim = []
    min_rounds_prim = []

    average_rounds_kruskal = []
    max_rounds_kruskal = []
    min_rounds_kruskal = []

    for size in sizes:
        size_avg_rounds_prim = 0
        size_max_rounds_prim = float("-inf")
        size_min_rounds_prim = float("inf")

        size_avg_rounds_kruskal = 0
        size_max_rounds_kruskal = float("-inf")
        size_min_rounds_kruskal = float("inf")

        for _ in range(num_graphs):
            graph = generate_random_graph(size)

            # Compute rounds for Prim's MST
            mst_prim = generate_mst_prim(graph)
            root = random.randint(0, size - 1)
            rounds_prim = compute_min_rounds(mst_prim, root)

            size_avg_rounds_prim += rounds_prim
            size_max_rounds_prim = max(size_max_rounds_prim, rounds_prim)
            size_min_rounds_prim = min(size_min_rounds_prim, rounds_prim)

            # Compute rounds for Kruskal's MST
            mst_kruskal = generate_mst_kruskal(graph)
            rounds_kruskal = compute_min_rounds(mst_kruskal, root)

            size_avg_rounds_kruskal += rounds_kruskal
            size_max_rounds_kruskal = max(size_max_rounds_kruskal, rounds_kruskal)
            size_min_rounds_kruskal = min(size_min_rounds_kruskal, rounds_kruskal)

        size_avg_rounds_prim /= num_graphs
        average_rounds_prim.append(size_avg_rounds_prim)
        max_rounds_prim.append(size_max_rounds_prim)
        min_rounds_prim.append(size_min_rounds_prim)

        size_avg_rounds_kruskal /= num_graphs
        average_rounds_kruskal.append(size_avg_rounds_kruskal)
        max_rounds_kruskal.append(size_max_rounds_kruskal)
        min_rounds_kruskal.append(size_min_rounds_kruskal)

    return (
        average_rounds_prim,
        max_rounds_prim,
        min_rounds_prim,
        average_rounds_kruskal,
        max_rounds_kruskal,
        min_rounds_kruskal,
    )


if __name__ == "__main__":
    num_graphs = 10  # Number of graphs to generate per size
    sizes = list(range(10, 1001, 10))  # Sizes of graphs to experiment with

    (
        avg_rounds_prim,
        max_rounds_prim,
        min_rounds_prim,
        avg_rounds_kruskal,
        max_rounds_kruskal,
        min_rounds_kruskal,
    ) = experiment(num_graphs, sizes)

    # Plotting results for Prim's MST
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(
        sizes,
        avg_rounds_prim,
        marker="o",
        linestyle="-",
        color="b",
        label="Average Rounds",
    )
    plt.plot(
        sizes,
        max_rounds_prim,
        marker="s",
        linestyle="--",
        color="r",
        label="Max Rounds",
    )
    plt.plot(
        sizes, min_rounds_prim, marker="^", linestyle=":", color="g", label="Min Rounds"
    )
    plt.title(
        "Prim's MST: Average Case Analysis of Rounds Needed for Information Dissemination"
    )
    plt.xlabel("Number of Vertices")
    plt.ylabel("Rounds")
    plt.xticks(sizes)
    plt.legend()
    plt.grid(True)

    # Plotting results for Kruskal's MST
    plt.subplot(1, 2, 2)
    plt.plot(
        sizes,
        avg_rounds_kruskal,
        marker="o",
        linestyle="-",
        color="b",
        label="Average Rounds",
    )
    plt.plot(
        sizes,
        max_rounds_kruskal,
        marker="s",
        linestyle="--",
        color="r",
        label="Max Rounds",
    )
    plt.plot(
        sizes,
        min_rounds_kruskal,
        marker="^",
        linestyle=":",
        color="g",
        label="Min Rounds",
    )
    plt.title(
        "Kruskal's MST: Average Case Analysis of Rounds Needed for Information Dissemination"
    )
    plt.xlabel("Number of Vertices")
    plt.ylabel("Rounds")
    plt.xticks(sizes)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("result.png")
    plt.show()
