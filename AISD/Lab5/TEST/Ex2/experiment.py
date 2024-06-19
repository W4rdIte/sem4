import time
import numpy as np
from graph import Graph

N_MIN = 10
N_MAX = 1000
STEP = 10
EXPERIMENT_REPEATS = 10


def run_experiment():
    results = []
    with open("results.txt", "w") as output_file:
        for current_n in range(N_MIN, N_MAX + STEP, STEP):
            print(f"Current N: {current_n}")

            info_rounds = []

            for _ in range(EXPERIMENT_REPEATS):
                graph = Graph.generate_random_complete_graph(current_n)

                # Generate MST using Kruskal's or Prim's
                mst = graph.generate_kruskals_minimum_spanning_tree()

                # Choose a random root node (0 for simplicity)
                root = 0

                # Calculate information transmission order
                rounds, max_round = mst.calculate_info_transmission_order(root)
                info_rounds.append(max_round)

            avg_rounds = sum(info_rounds) / len(info_rounds)
            min_rounds = min(info_rounds)
            max_rounds = max(info_rounds)

            output_file.write(
                f"{current_n} {avg_rounds:.2f} {min_rounds} {max_rounds}\n"
            )


if __name__ == "__main__":
    run_experiment()
