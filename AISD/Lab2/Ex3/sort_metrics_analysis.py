import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("sort_c&s.txt", dtype=str)

# Separate data by sorting algorithm
sorting_data = {"y": [], "m": []}
for row in data:
    sorting_data[row[0]].append(row[1:].astype(int))

# Calculate average number of comparisons and swaps for each n
averages = {
    "n": [],
    "c_y": [],
    "c_m": [],
    "c_h": [],
    "s_y": [],
    "s_m": [],
    "s_h": [],
    "c/n_i": [],
    "c/n_q": [],
    "c/n_h": [],
    "s/n_i": [],
    "s/n_q": [],
    "s/n_h": [],
}
for n in range(10, 51, 10):
    c_y = 0
    c_m = 0
    s_y = 0
    s_m = 0
    count_y = 0
    count_m = 0
    for row in sorting_data["y"]:
        if row[0] == n:
            c_y += row[1]
            s_y += row[2]
            count_y += 1
    for row in sorting_data["m"]:
        if row[0] == n:
            c_m += row[1]
            s_m += row[2]
            count_m += 1

    averages["n"].append(n)
    averages["c_y"].append(c_y / count_y if count_y != 0 else 0)
    averages["c_m"].append(c_m / count_m if count_m != 0 else 0)
    averages["s_y"].append(s_y / count_y if count_y != 0 else 0)
    averages["s_m"].append(s_m / count_m if count_m != 0 else 0)
    averages["c/n_i"].append((c_y / n) if n != 0 else 0)
    averages["c/n_q"].append((c_m / n) if n != 0 else 0)
    averages["s/n_i"].append((s_y / n) if n != 0 else 0)
    averages["s/n_q"].append((s_m / n) if n != 0 else 0)

# Plotting
plt.figure(figsize=(18, 6))

# Average number of comparisons
plt.subplot(1, 3, 1)
plt.plot(averages["n"], averages["c_y"], label="Insertion Sort")
plt.plot(averages["n"], averages["c_m"], label="Quick Sort")
plt.title("Average Comparisons vs. n")
plt.xlabel("n")
plt.ylabel("Average Comparisons")
plt.legend()

# Average number of swaps
plt.subplot(1, 3, 2)
plt.plot(averages["n"], averages["s_y"], label="Insertion Sort")
plt.plot(averages["n"], averages["s_m"], label="Quick Sort")
plt.title("Average Swaps vs. n")
plt.xlabel("n")
plt.ylabel("Average Swaps")
plt.legend()

# c/n and s/n ratios
plt.subplot(1, 3, 3)
plt.plot(averages["n"], averages["c/n_i"], label="Insertion Sort (c/n)")
plt.plot(averages["n"], averages["c/n_q"], label="Quick Sort (c/n)")
plt.plot(averages["n"], averages["s/n_i"], label="Insertion Sort (s/n)")
plt.plot(averages["n"], averages["s/n_q"], label="Quick Sort (s/n)")
plt.title("Comparison and Swap Ratios vs. n")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.legend()

plt.tight_layout()
plt.show()
