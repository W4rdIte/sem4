import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("results.txt")

graph_size = data[:, 0]
kruskal_duration = data[:, 1]
prim_duration = data[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(graph_size, kruskal_duration, label="Kruskal's Algorithm")
plt.plot(graph_size, prim_duration, label="Prim's Algorithm")

plt.title("MST Generation Time Comparison")
plt.xlabel("Graph Size (n)")
plt.ylabel("Duration in nanoseconds")
plt.legend()

plt.savefig("results.png")
plt.show()
