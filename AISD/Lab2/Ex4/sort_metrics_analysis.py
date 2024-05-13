import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("sort_c&s.txt", dtype=str)

# Separate data by sorting algorithm
sorting_data = {"q": [], "d": []}
for row in data:
    sorting_data[row[0]].append(row[1:].astype(int))

# Calculate average number of comparisons and swaps for each n
averages = {
    "n": [],
    "c_q": [],
    "c_d": [],
    "s_q": [],
    "s_d": [],
    "c/n_q": [],
    "c/n_d": [],
    "s/n_q": [],
    "s/n_d": [],
}
for n in range(10, 51, 10):
    c_q = 0
    c_d = 0
    s_q = 0
    s_d = 0
    count_q = 0
    count_d = 0
    for row in sorting_data["q"]:
        if row[0] == n:
            c_q += row[1]
            s_q += row[2]
            count_q += 1
    for row in sorting_data["d"]:
        if row[0] == n:
            c_d += row[1]
            s_d += row[2]
            count_d += 1

    averages["n"].append(n)
    averages["c_q"].append(c_q / count_q if count_q != 0 else 0)
    averages["c_d"].append(c_d / count_d if count_d != 0 else 0)
    averages["s_q"].append(s_q / count_q if count_q != 0 else 0)
    averages["s_d"].append(s_d / count_d if count_d != 0 else 0)
    averages["c/n_q"].append((c_q / n) if n != 0 else 0)
    averages["c/n_d"].append((c_d / n) if n != 0 else 0)
    averages["s/n_q"].append((s_q / n) if n != 0 else 0)
    averages["s/n_d"].append((s_d / n) if n != 0 else 0)

# Plotting
plt.figure(figsize=(18, 6))

# Average number of comparisons
plt.subplot(1, 3, 1)
plt.plot(averages["n"], averages["c_q"], label="Quick Sort")
plt.plot(averages["n"], averages["c_d"], label="Dual Pivot")
plt.title("Average Comparisons vs. n")
plt.xlabel("n")
plt.ylabel("Average Comparisons")
plt.legend()

# Average number of swaps
plt.subplot(1, 3, 2)
plt.plot(averages["n"], averages["s_q"], label="Quick Sort")
plt.plot(averages["n"], averages["s_d"], label="Dual Pivot")
plt.title("Average Swaps vs. n")
plt.xlabel("n")
plt.ylabel("Average Swaps")
plt.legend()

# c/n and s/n ratios
plt.subplot(1, 3, 3)
plt.plot(averages["n"], averages["c/n_q"], label="Quick Sort (c/n)")
plt.plot(averages["n"], averages["c/n_d"], label="Dual Pivot (c/n)")
plt.plot(averages["n"], averages["s/n_q"], label="Quick Sort (s/n)")
plt.plot(averages["n"], averages["s/n_d"], label="Dual Pivot (s/n)")
plt.title("Comparison and Swap Ratios vs. n")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.legend()

plt.tight_layout()
plt.show()
