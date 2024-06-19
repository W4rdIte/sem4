import matplotlib.pyplot as plt
import random
import time

# Importujemy zmodyfikowaną klasę BST

# Tutaj importujemy klasy BST i Node z odpowiednimi zmianami
from BST import BST, Node


# Funkcja do generowania danych testowych
def generate_data(n):
    return random.sample(range(1, 10 * n), n)


# Funkcja do przeprowadzania eksperymentu dla określonej wielkości danych
def run_experiment(n):
    bst = BST()
    data = generate_data(n)

    comparisons = []
    pointer_ops = []
    heights = []

    # Wstawianie rosnącego ciągu
    for key in data:
        bst.insert(key)
        metrics = bst.get_metrics()
        comparisons.append(metrics["comparisons"])
        pointer_ops.append(metrics["pointer_ops"])
        heights.append(metrics["height"])

    # Usuwanie losowego ciągu
    random.shuffle(data)
    for key in data:
        bst.delete(key)
        metrics = bst.get_metrics()
        comparisons.append(metrics["comparisons"])
        pointer_ops.append(metrics["pointer_ops"])
        heights.append(metrics["height"])

    return comparisons, pointer_ops, heights


# Funkcja do przeprowadzenia eksperymentów dla różnych wartości n
def run_experiments():
    ns = list(range(10000, 20001, 10000))
    avg_comparisons = []
    max_comparisons = []
    avg_pointer_ops = []
    max_pointer_ops = []
    avg_heights = []
    max_heights = []

    for n in ns:
        all_comparisons = []
        all_pointer_ops = []
        all_heights = []
        for _ in range(20):
            comparisons, pointer_ops, heights = run_experiment(n)
            all_comparisons.extend(comparisons)
            all_pointer_ops.extend(pointer_ops)
            all_heights.extend(heights)

        avg_comparisons.append(sum(all_comparisons) / len(all_comparisons))
        max_comparisons.append(max(all_comparisons))
        avg_pointer_ops.append(sum(all_pointer_ops) / len(all_pointer_ops))
        max_pointer_ops.append(max(all_pointer_ops))
        avg_heights.append(sum(all_heights) / len(all_heights))
        max_heights.append(max(all_heights))

    return (
        ns,
        avg_comparisons,
        max_comparisons,
        avg_pointer_ops,
        max_pointer_ops,
        avg_heights,
        max_heights,
    )


# Wywołujemy eksperymenty i pobieramy wyniki
(
    ns,
    avg_comparisons,
    max_comparisons,
    avg_pointer_ops,
    max_pointer_ops,
    avg_heights,
    max_heights,
) = run_experiments()

# Generujemy wykresy dla każdej z miar złożoności
plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.plot(ns, avg_comparisons, label="Average Comparisons")
plt.plot(ns, max_comparisons, label="Max Comparisons")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Comparisons")
plt.title("Complexity Analysis - Comparisons")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(ns, avg_pointer_ops, label="Average Pointer Operations")
plt.plot(ns, max_pointer_ops, label="Max Pointer Operations")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Pointer Operations")
plt.title("Complexity Analysis - Pointer Operations")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(ns, avg_heights, label="Average Height")
plt.plot(ns, max_heights, label="Max Height")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Height")
plt.title("Complexity Analysis - Height")
plt.legend()

plt.tight_layout()
plt.show()
