import os
import subprocess

from utils import test_run


def run_experiment(times):
    n_values = [i for i in range(test_run.min_n, test_run.max_n, test_run.step)]

    for t in range(times):
        for n in n_values:
            for algorithm in [
                "select.py",
                # "randomized_select.py",
            ]:
                with open("data_generator_output.txt", "w") as file:
                    subprocess.run(
                        ["python3", "data_generator.py", str(n)], stdout=file
                    )

                subprocess.run(
                    ["python3", algorithm, str(test_run.k), str(n)]
                )  # Pass n as an argument here
                os.remove("data_generator_output.txt")


# Run experiments
if os.path.exists(test_run.output_file):
    os.remove(test_run.output_file)

run_experiment(50)
