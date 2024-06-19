import numpy as np
import matplotlib.pyplot as plt

from utils import test_run

# Load data from file
data = np.loadtxt(test_run.output_file, dtype=str)

# Separate data by sorting algorithm
sorting_data = {"3": [], "5": [], "7": [], "9": []}
for row in data:
    key = row[-1]  # Get the last element in the row
    sorting_data[key].append(
        row[1:].astype(int)
    )  # Append row without the algorithm identifier

# Calculate average number of comparisons and swaps for each n
averages = {
    "n": {"3": [], "5": [], "7": [], "9": []},
    "c_s": {"3": [], "5": [], "7": [], "9": []},
    "s_s": {"3": [], "5": [], "7": [], "9": []},
}
for n in range(test_run.min_n, test_run.max_n, test_run.step):
    for key in sorting_data.keys():
        c_s = 0
        s_s = 0
        count_s = 0

        for row in sorting_data[key]:
            if row[0] == n:
                c_s += row[1]
                s_s += row[2]
                count_s += 1

        averages["n"][key].append(n)
        averages["c_s"][key].append(c_s / count_s if count_s != 0 else 0)
        averages["s_s"][key].append(s_s / count_s if count_s != 0 else 0)

# Plotting
plt.figure(figsize=(18, 6))

# Average number of comparisons
plt.subplot(1, 2, 1)
for key in sorting_data.keys():
    plt.plot(averages["n"][key], averages["c_s"][key], label=f"Algorithm {key}")
plt.title("Average Comparisons vs. n")
plt.xlabel("n")
plt.ylabel("Average Comparisons")
plt.legend()

# Average number of swaps
plt.subplot(1, 2, 2)
for key in sorting_data.keys():
    plt.plot(averages["n"][key], averages["s_s"][key], label=f"Algorithm {key}")
plt.title("Average Swaps vs. n")
plt.xlabel("n")
plt.ylabel("Average Swaps")
plt.legend()

plt.savefig("sorting_analysis.png")
plt.tight_layout()
plt.show()
