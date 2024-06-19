import time
import numpy as np
from Graph import Graph
from statistics import mean

N_MIN = 10
N_MAX = 1000
STEP = 10
EXPERIMENT_REPEATS = 10


def run_experiment():
    with open("plots/durations.txt", "w") as output_file:
        for current_n in range(N_MIN, N_MAX + 1, STEP):
            print(f"Current N: {current_n}")

            kruskal_durations = []
            prim_durations = []

            for _ in range(EXPERIMENT_REPEATS):
                graph = Graph.generate_random_complete_graph(current_n)

                start_time = time.time()
                graph.generate_kruskals_minimum_spanning_tree()
                kruskal_durations.append((time.time() - start_time) * 1e9)

                start_time = time.time()
                graph.generate_prims_minimum_spanning_tree()
                prim_durations.append((time.time() - start_time) * 1e9)

            kruskal_duration = mean(kruskal_durations)
            prim_duration = mean(prim_durations)

            output_file.write(f"{current_n} {kruskal_duration} {prim_duration}\n")


if __name__ == "__main__":
    run_experiment()
