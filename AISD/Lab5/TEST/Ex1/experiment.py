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

            kruskal_duration = 0
            prim_duration = 0

            for _ in range(EXPERIMENT_REPEATS):
                graph = Graph.generate_random_complete_graph(current_n)

                start_time = time.perf_counter()
                graph.generate_kruskals_minimum_spanning_tree()
                kruskal_duration += time.perf_counter() - start_time

                start_time = time.perf_counter()
                graph.generate_prims_minimum_spanning_tree()
                prim_duration += time.perf_counter() - start_time

            kruskal_duration /= EXPERIMENT_REPEATS
            prim_duration /= EXPERIMENT_REPEATS

            output_file.write(
                f"{current_n} {kruskal_duration:.9f} {prim_duration:.9f}\n"
            )


if __name__ == "__main__":
    run_experiment()
