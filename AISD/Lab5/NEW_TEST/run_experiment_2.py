import time
import numpy as np
from Graph import Graph
from statistics import mean

N_MIN = 10
N_MAX = 1000
STEP = 10
EXPERIMENT_REPEATS = 10


def run_experiment():
    with open("plots/rounds.txt", "w") as output_file:
        for current_n in range(N_MIN, N_MAX + 1, STEP):
            print(f"Current N: {current_n}")

            average_rounds = 0
            min_rounds = 0
            max_rounds = 0

            for _ in range(EXPERIMENT_REPEATS):
                graph = Graph.generate_random_complete_graph(
                    current_n
                ).generate_prims_minimum_spanning_tree()

                current_min = float("inf")
                current_max = float("-inf")

                for node in range(current_n):
                    _, rounds_left = graph.find_shortest_info_spread_order(node)
                    rounds = rounds_left[node]

                    average_rounds += rounds
                    current_min = min(current_min, rounds)
                    current_max = max(current_max, rounds)

                min_rounds += current_min
                max_rounds += current_max

            average_rounds /= EXPERIMENT_REPEATS * current_n
            min_rounds /= EXPERIMENT_REPEATS
            max_rounds /= EXPERIMENT_REPEATS

            output_file.write(
                f"{current_n} {average_rounds:.2f} {min_rounds:.2f} {max_rounds:.2f}\n"
            )


if __name__ == "__main__":
    run_experiment()
