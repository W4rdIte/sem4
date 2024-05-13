import random
import sys

# Globalne liczniki
comparisons = 0
swaps = 0

def print_state(arr, msg=""):
    print(f"{msg}{arr}")

# INSERTION SORT z wypisywaniem stanów tablicy
def insertion_sort(arr):
    global comparisons, swaps
    print_state(arr, "Initial state: ")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        if j >= 0: comparisons += 1
        print_state(arr, "After inserting key {}: ".format(key))

# QUICK SORT
def quick_sort(arr, low, high, initial_call=True):
    # Wyświetlanie stanu początkowego tablicy tylko przy pierwszym wywołaniu
    if initial_call:
        print_state(arr, "Initial unsorted array: ")
    if low < high:
        pi = partition(arr, low, high)
        print_state(arr, f"After partitioning with pivot {arr[pi]}: ")
        quick_sort(arr, low, pi - 1, False)  # Ustawienie initial_call na False dla wywołań rekurencyjnych
        quick_sort(arr, pi + 1, high, False)


def partition(arr, low, high):
    global comparisons, swaps
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    swaps += 1
    return i+1

# Hybrid QUICK SORT with INSERTION SORT for small subarrays
def hybrid_quick_sort(arr, low, high, threshold=10, initial_call=True):
    # Wyświetlanie stanu początkowego tablicy tylko przy pierwszym wywołaniu
    if initial_call:
        print_state(arr, "Initial unsorted array: ")
    if low < high:
        if high - low < threshold:
            print_state(arr[low:high+1], "Small subarray (using Insertion Sort): ")
            insertion_sort_part(arr, low, high)
            print_state(arr[low:high+1], "After sorting small subarray: ")
        else:
            pi = partition(arr, low, high)
            print_state(arr, f"After partitioning with pivot {arr[pi]}: ")
            hybrid_quick_sort(arr, low, pi - 1, threshold, False)  # Ustawienie initial_call na False dla wywołań rekurencyjnych
            hybrid_quick_sort(arr, pi + 1, high, threshold, False)


def insertion_sort_part(arr, low, high):
    global comparisons, swaps
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i-1
        while j >= low and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        if j >= low: comparisons += 1

# Data generators
def generate_random_keys(n):
    return [random.randint(0, 2*n-1) for _ in range(n)]

def generate_ascending_keys(n):
    return [i for i in range(n)]

def generate_descending_keys(n):
    return [i for i in reversed(range(n))]

def run_sorting_algorithm(algorithm_name, data):
    global comparisons, swaps
    comparisons = 0
    swaps = 0

    if algorithm_name == "insertion_sort":
        insertion_sort(data)
        print("After sorting (Insertion Sort): ", data)

    elif algorithm_name == "quick_sort":
        quick_sort(data, 0, len(data) - 1)
        print("After sorting (Quick Sort): ", data)

    elif algorithm_name == "hybrid_quick_sort":
        hybrid_quick_sort(data, 0, len(data) - 1)
        print("After sorting (Hybrid Quick Sort): ", data)

    else:
        print(f"Algorithm '{algorithm_name}' is not recognized.")

    print("Comparisons:", comparisons, "Swaps:", swaps)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <script_name> <data_type> <n> <algorithm_name>")
        sys.exit(1)
    
    data_type = sys.argv[1]
    n = int(sys.argv[2])
    algorithm_name = sys.argv[3]

    data_generators = {
        "random": generate_random_keys,
        "ascending": generate_ascending_keys,
        "descending": generate_descending_keys
    }

    if data_type not in data_generators:
        print("Invalid data type. Choose from 'random', 'ascending', 'descending'.")
        sys.exit(1)

    data = data_generators[data_type](n)
    run_sorting_algorithm(algorithm_name, data)
