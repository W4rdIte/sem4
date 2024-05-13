import os
import subprocess

output_file = "sort_c&s.txt"


def run_experiment(k_values):
    n_values = [10 * i for i in range(1, 6)]

    for k in range(k_values):
        for n in n_values:
            for algorithm in [
                "quick_sort.py",
                "dual_pivot_quicksort.py",
            ]:
                with open("data_generator_output.txt", "w") as file:
                    subprocess.run(
                        ["python3", "data_generator.py", str(n)], stdout=file
                    )

                with open("data_generator_output.txt", "r") as file:
                    subprocess.run(["python3", algorithm], stdin=file)
            os.remove("data_generator_output.txt")


# Run experiments
if os.path.exists(output_file):
    os.remove(output_file)

run_experiment(1)
