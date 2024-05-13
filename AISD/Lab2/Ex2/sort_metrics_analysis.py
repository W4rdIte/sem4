import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("sort_c&s.txt", dtype=str)

# Separate data by sorting algorithm
sorting_data = {"i": [], "q": [], "h": []}
for row in data:
    sorting_data[row[0]].append(row[1:].astype(int))

# Calculate average number of comparisons and swaps for each n
averages = {
    "n": [],
    "c_i": [],
    "c_q": [],
    "c_h": [],
    "s_i": [],
    "s_q": [],
    "s_h": [],
    "c/n_i": [],
    "c/n_q": [],
    "c/n_h": [],
    "s/n_i": [],
    "s/n_q": [],
    "s/n_h": [],
}
for n in range(10, 51, 10):
    c_i = 0
    c_q = 0
    c_h = 0
    s_i = 0
    s_q = 0
    s_h = 0
    count_i = 0
    count_q = 0
    count_h = 0
    for row in sorting_data["i"]:
        if row[0] == n:
            c_i += row[1]
            s_i += row[2]
            count_i += 1
    for row in sorting_data["q"]:
        if row[0] == n:
            c_q += row[1]
            s_q += row[2]
            count_q += 1
    for row in sorting_data["h"]:
        if row[0] == n:
            c_h += row[1]
            s_h += row[2]
            count_h += 1
    averages["n"].append(n)
    averages["c_i"].append(c_i / count_i if count_i != 0 else 0)
    averages["c_q"].append(c_q / count_q if count_q != 0 else 0)
    averages["c_h"].append(c_h / count_h if count_h != 0 else 0)
    averages["s_i"].append(s_i / count_i if count_i != 0 else 0)
    averages["s_q"].append(s_q / count_q if count_q != 0 else 0)
    averages["s_h"].append(s_h / count_h if count_h != 0 else 0)
    averages["c/n_i"].append((c_i / n) if n != 0 else 0)
    averages["c/n_q"].append((c_q / n) if n != 0 else 0)
    averages["c/n_h"].append((c_h / n) if n != 0 else 0)
    averages["s/n_i"].append((s_i / n) if n != 0 else 0)
    averages["s/n_q"].append((s_q / n) if n != 0 else 0)
    averages["s/n_h"].append((s_h / n) if n != 0 else 0)

# Plotting
plt.figure(figsize=(18, 6))

# Average number of comparisons
plt.subplot(1, 3, 1)
plt.plot(averages["n"], averages["c_i"], label="Insertion Sort")
plt.plot(averages["n"], averages["c_q"], label="Quick Sort")
plt.plot(averages["n"], averages["c_h"], label="Hybrid Sort")
plt.title("Average Comparisons vs. n")
plt.xlabel("n")
plt.ylabel("Average Comparisons")
plt.legend()

# Average number of swaps
plt.subplot(1, 3, 2)
plt.plot(averages["n"], averages["s_i"], label="Insertion Sort")
plt.plot(averages["n"], averages["s_q"], label="Quick Sort")
plt.plot(averages["n"], averages["s_h"], label="Hybrid Sort")
plt.title("Average Swaps vs. n")
plt.xlabel("n")
plt.ylabel("Average Swaps")
plt.legend()

# c/n and s/n ratios
plt.subplot(1, 3, 3)
plt.plot(averages["n"], averages["c/n_i"], label="Insertion Sort (c/n)")
plt.plot(averages["n"], averages["c/n_q"], label="Quick Sort (c/n)")
plt.plot(averages["n"], averages["c/n_h"], label="Hybrid Sort (c/n)")
plt.plot(averages["n"], averages["s/n_i"], label="Insertion Sort (s/n)")
plt.plot(averages["n"], averages["s/n_q"], label="Quick Sort (s/n)")
plt.plot(averages["n"], averages["s/n_h"], label="Hybrid Sort (s/n)")
plt.title("Comparison and Swap Ratios vs. n")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.legend()

plt.tight_layout()
plt.show()
