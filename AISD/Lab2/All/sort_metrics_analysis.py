import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("sort_c&s.txt", dtype=str)

# Separate data by sorting algorithm
sorting_data = {"d": [], "h": [], "m": [], "y": [], "q": []}
for row in data:
    sorting_data[row[0]].append(row[1:].astype(int))

# Calculate average number of comparisons and swaps for each n
averages = {
    "n": [],
    "c_d": [],
    "c_h": [],
    "c_m": [],
    "c_y": [],
    "c_q": [],
    "s_d": [],
    "s_h": [],
    "s_m": [],
    "s_y": [],
    "s_q": [],
    "c/n_d": [],
    "c/n_h": [],
    "c/n_m": [],
    "c/n_y": [],
    "c/n_q": [],
    "s/n_d": [],
    "s/n_h": [],
    "s/n_m": [],
    "s/n_y": [],
    "s/n_q": [],
}

for n in range(10, 51, 10):
    c_d = 0
    c_h = 0
    c_m = 0
    c_y = 0
    c_q = 0

    s_d = 0
    s_h = 0
    s_m = 0
    s_y = 0
    s_q = 0

    count_d = 0
    count_h = 0
    count_m = 0
    count_y = 0
    count_q = 0

    for row in sorting_data["d"]:
        if row[0] == n:
            c_d += row[1]
            s_d += row[2]
            count_d += 1
    for row in sorting_data["h"]:
        if row[0] == n:
            c_h += row[1]
            s_h += row[2]
            count_h += 1
    for row in sorting_data["m"]:
        if row[0] == n:
            c_m += row[1]
            s_m += row[2]
            count_m += 1
    for row in sorting_data["y"]:
        if row[0] == n:
            c_y += row[1]
            s_y += row[2]
            count_y += 1
    for row in sorting_data["q"]:
        if row[0] == n:
            c_q += row[1]
            s_q += row[2]
            count_q += 1

    averages["n"].append(n)

    if count_d != 0:
        averages["c_d"].append(c_d / count_d)
        averages["s_d"].append(s_d / count_d)
        averages["c/n_d"].append(c_d / n)
        averages["s/n_d"].append(s_d / n)
    else:
        averages["c_d"].append(0)
        averages["s_d"].append(0)
        averages["c/n_d"].append(0)
        averages["s/n_d"].append(0)

    if count_h != 0:
        averages["c_h"].append(c_h / count_h)
        averages["s_h"].append(s_h / count_h)
        averages["c/n_h"].append(c_h / n)
        averages["s/n_h"].append(s_h / n)
    else:
        averages["c_h"].append(0)
        averages["s_h"].append(0)
        averages["c/n_h"].append(0)
        averages["s/n_h"].append(0)

    if count_m != 0:
        averages["c_m"].append(c_m / count_m)
        averages["s_m"].append(s_m / count_m)
        averages["c/n_m"].append(c_m / n)
        averages["s/n_m"].append(s_m / n)
    else:
        averages["c_m"].append(0)
        averages["s_m"].append(0)
        averages["c/n_m"].append(0)
        averages["s/n_m"].append(0)

    if count_y != 0:
        averages["c_y"].append(c_y / count_y)
        averages["s_y"].append(s_y / count_y)
        averages["c/n_y"].append(c_y / n)
        averages["s/n_y"].append(s_y / n)
    else:
        averages["c_y"].append(0)
        averages["s_y"].append(0)
        averages["c/n_y"].append(0)
        averages["s/n_y"].append(0)

    if count_q != 0:
        averages["c_q"].append(c_q / count_q)
        averages["s_q"].append(s_q / count_q)
        averages["c/n_q"].append(c_q / n)
        averages["s/n_q"].append(s_q / n)
    else:
        averages["c_q"].append(0)
        averages["s_q"].append(0)
        averages["c/n_q"].append(0)
        averages["s/n_q"].append(0)

# Plotting
plt.figure(figsize=(18, 6))

# Average number of comparisons
plt.subplot(1, 3, 1)
plt.plot(averages["n"], averages["c_d"], label="Dual Pivot")
plt.plot(averages["n"], averages["c_h"], label="Hybrid Sort")
plt.plot(averages["n"], averages["c_m"], label="Merge Sort")
plt.plot(averages["n"], averages["c_y"], label="My Sort")
plt.plot(averages["n"], averages["c_q"], label="Quick Sort")
plt.title("Average Comparisons vs. n")
plt.xlabel("n")
plt.ylabel("Average Comparisons")
plt.legend()

# Average number of swaps
plt.subplot(1, 3, 2)
plt.plot(averages["n"], averages["s_d"], label="Dual Pivot")
plt.plot(averages["n"], averages["s_h"], label="Hybrid Sort")
plt.plot(averages["n"], averages["s_m"], label="Merge Sort")
plt.plot(averages["n"], averages["s_y"], label="My Sort")
plt.plot(averages["n"], averages["s_q"], label="Quick Sort")
plt.title("Average Swaps vs. n")
plt.xlabel("n")
plt.ylabel("Average Swaps")
plt.legend()

# c/n and s/n ratios
plt.subplot(1, 3, 3)
plt.plot(averages["n"], averages["c/n_d"], label="Dual Pivot (c/n)")
plt.plot(averages["n"], averages["c/n_h"], label="Hybrid Sort (c/n)")
plt.plot(averages["n"], averages["c/n_m"], label="Merge Sort (c/n)")
plt.plot(averages["n"], averages["c/n_y"], label="My Sort (c/n)")
plt.plot(averages["n"], averages["c/n_q"], label="Quick Sort (c/n)")

plt.plot(averages["n"], averages["s/n_d"], label="Dual Pivot (s/n)")
plt.plot(averages["n"], averages["s/n_h"], label="Hybrid Sort (s/n)")
plt.plot(averages["n"], averages["s/n_m"], label="Merge Sort (s/n)")
plt.plot(averages["n"], averages["s/n_y"], label="My Sort (s/n)")
plt.plot(averages["n"], averages["s/n_q"], label="Quick Sort (s/n)")
plt.title("Comparison and Swap Ratios vs. n")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.legend()

plt.tight_layout()

# Save plot as .png
plt.savefig("sorting_analysis.png")

# Save plot as .jpg
# plt.savefig("sorting_analysis.jpg")

plt.show()
