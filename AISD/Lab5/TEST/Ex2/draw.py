import matplotlib.pyplot as plt


def main():
    file_path = "results.txt"
    data = {"N": [], "Average Rounds": [], "Min Rounds": [], "Max Rounds": []}

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                current_n, avg_rounds, min_rounds, max_rounds = parts
                data["N"].append(int(current_n))
                data["Average Rounds"].append(float(avg_rounds))
                data["Min Rounds"].append(int(min_rounds))
                data["Max Rounds"].append(int(max_rounds))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(
        data["N"],
        data["Average Rounds"],
        marker="o",
        linestyle="-",
        color="b",
        label="Average Rounds",
    )
    plt.errorbar(
        data["N"],
        data["Average Rounds"],
        yerr=[
            data["Average Rounds"][i] - data["Min Rounds"][i]
            for i in range(len(data["N"]))
        ],
        fmt="none",
        ecolor="g",
        capsize=5,
        label="Min Rounds",
    )
    plt.errorbar(
        data["N"],
        data["Average Rounds"],
        yerr=[
            data["Max Rounds"][i] - data["Average Rounds"][i]
            for i in range(len(data["N"]))
        ],
        fmt="none",
        ecolor="r",
        capsize=5,
        label="Max Rounds",
    )

    plt.title("Average Case Analysis of Information Transmission Rounds")
    plt.xlabel("Number of Vertices (N)")
    plt.ylabel("Rounds")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results.png")
    plt.show()


if __name__ == "__main__":
    main()
