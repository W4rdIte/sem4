import numpy as np
import matplotlib.pyplot as plt

from utils import test_run

# Load data from file
data = np.loadtxt(test_run.output_file, dtype=str)

# Separate data by sorting algorithm
sorting_data = {"s": [], "r": []}
for row in data:
    sorting_data[row[0]].append(row[1:].astype(int))

# Calculate average number of comparisons and swaps for each n
averages = {
    "n": [],
    "c_s": [],
    "c_r": [],
    "s_s": [],
    "s_r": [],
}
for n in range(test_run.min_n, test_run.max_n, test_run.step):
    c_s = 0
    c_r = 0
    s_s = 0
    s_r = 0
    count_s = 0
    count_r = 0
    for row in sorting_data["s"]:
        if row[0] == n:
            c_s += row[1]
            s_s += row[2]
            count_s += 1
    for row in sorting_data["r"]:
        if row[0] == n:
            c_r += row[1]
            s_r += row[2]
            count_r += 1

    print(
        f"n={n}: c_s={c_s / count_s if count_s != 0 else 0}, c_r={c_r / count_r if count_r != 0 else 0}, s_s={s_s / count_s if count_s != 0 else 0}, s_r={s_r / count_r if count_r != 0 else 0}"
    )

    averages["n"].append(n)
    averages["c_s"].append(c_s / count_s if count_s != 0 else 0)
    averages["c_r"].append(c_r / count_r if count_r != 0 else 0)
    averages["s_s"].append(s_s / count_s if count_s != 0 else 0)
    averages["s_r"].append(s_r / count_r if count_r != 0 else 0)

# Plotting
plt.figure(figsize=(18, 6))

# Average number of comparisons
plt.subplot(1, 3, 1)
plt.plot(averages["n"], averages["c_s"], label="Select")
plt.plot(averages["n"], averages["c_r"], label="Randomized Select")
plt.title("Average Comparisons vs. n")
plt.xlabel("n")
plt.ylabel("Average Comparisons")
plt.legend()

# Average number of swaps
plt.subplot(1, 3, 2)
plt.plot(averages["n"], averages["s_s"], label="Select")
plt.plot(averages["n"], averages["s_r"], label="Randomized Select")
plt.title("Average Swaps vs. n")
plt.xlabel("n")
plt.ylabel("Average Swaps")
plt.legend()

plt.savefig("sorting_analysis.png")
plt.tight_layout()
plt.show()
