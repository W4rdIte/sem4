import time
import random
import matplotlib.pyplot as plt
from functions import binary_search


def test_binary_search(n, v):
    arr = list(range(1, n + 1))
    comparisons = 0

    start_time = time.time()
    result = binary_search(arr, 0, len(arr) - 1, v)
    end_time = time.time()

    return result, end_time - start_time


# Testowanie dla różnych rozmiarów tablicy i wartości v
sizes = range(1000, 100001, 1000)
v_values = [1, 500, 1000, 50000, 100000, 110000]

results = {v: {"comparisons": [], "time": []} for v in v_values}

for size in sizes:
    for v in v_values:
        avg_comparisons = 0
        avg_time = 0
        repetitions = 10

        for _ in range(repetitions):
            result, exec_time = test_binary_search(size, v)
            avg_comparisons += result
            avg_time += exec_time

        avg_comparisons /= repetitions
        avg_time /= repetitions

        results[v]["comparisons"].append(avg_comparisons)
        results[v]["time"].append(avg_time)

# Wykresy
for v in v_values:
    plt.plot(sizes, results[v]["comparisons"], label=f"v={v}")

plt.xlabel("Rozmiar tablicy (n)")
plt.ylabel("Liczba porównań")
plt.title("Liczba porównań dla różnych wartości v")
plt.legend()
plt.show()

for v in v_values:
    plt.plot(sizes, results[v]["time"], label=f"v={v}")

plt.xlabel("Rozmiar tablicy (n)")
plt.ylabel("Czas wykonania (s)")
plt.title("Czas wykonania dla różnych wartości v")
plt.legend()
plt.show()
