import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.loadtxt("plots/rounds.txt")

df = pd.DataFrame(data, columns=["N", "Average Rounds", "Min Rounds", "Max Rounds"])

plt.figure(figsize=(10, 6))

plt.plot(df["N"], df["Average Rounds"], label="Average Rounds", marker="o")

plt.plot(df["N"], df["Min Rounds"], label="Min Rounds", linestyle="--", marker="s")

plt.plot(df["N"], df["Max Rounds"], label="Max Rounds", linestyle="-.", marker="^")

plt.xlabel("N")
plt.ylabel("Rounds")
plt.title("Average, Min, and Max Rounds vs. N")
plt.legend()

plt.grid(True)

plt.tight_layout()
plt.savefig("img/results_experiment_2.png")
