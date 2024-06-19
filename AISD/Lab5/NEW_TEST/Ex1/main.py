import numpy as np
from Graph import Graph

GRAPH_SIZE = 10


def print_adjacency_matrix(adjacency_matrix: np.ndarray):
    for row in adjacency_matrix:
        for element in row:
            print(f"{element:8.2f}", end=" ")
        print()


def main():
    graph = Graph.generate_random_complete_graph(GRAPH_SIZE)

    print("Random complete graph:")
    print_adjacency_matrix(graph.get_adjacency_matrix())

    print("\nKruskal's minimum spanning tree:")
    print_adjacency_matrix(
        graph.generate_kruskals_minimum_spanning_tree().get_adjacency_matrix()
    )

    print("\nPrim's minimum spanning tree:")
    print_adjacency_matrix(
        graph.generate_prims_minimum_spanning_tree().get_adjacency_matrix()
    )

    print("\nOrder of shortest information spread starting from node 0:")
    order, rounds_left = (
        graph.generate_prims_minimum_spanning_tree().find_shortest_info_spread_order(0)
    )
    for i in range(GRAPH_SIZE):
        print(
            f"Node {i} -> next nodes: [ {' '.join(map(str, order[i]))} ], rounds left: {rounds_left[i]}"
        )


if __name__ == "__main__":
    main()
