import random
import matplotlib.pyplot as plt
from mst import Graph, compute_min_rounds


def generate_random_graph(size):
    graph = Graph(size)
    edges = []
    for i in range(size):
        for j in range(i + 1, size):
            if random.random() < 0.5:  # Probability of having an edge
                weight = random.randint(1, 100)  # Random weight
                edges.append((i, j, weight))

    for edge in edges:
        graph.add_weighted_edge(edge[0], edge[1], edge[2])

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
    sizes = [10, 20, 30, 40, 50]  # Sizes of graphs to experiment with

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
    plt.show()
