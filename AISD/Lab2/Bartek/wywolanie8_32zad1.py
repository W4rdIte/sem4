import random

# Globalne liczniki
comparisons = 0
swaps = 0

# INSERTION SORT
def insertion_sort(arr):
    global comparisons, swaps
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        if j >= 0: comparisons += 1

# QUICK SORT
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

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
def hybrid_quick_sort(arr, low, high, threshold=10):
    if low < high:
        if high - low < threshold:
            insertion_sort_part(arr, low, high)
        else:
            pi = partition(arr, low, high)
            hybrid_quick_sort(arr, low, pi-1, threshold)
            hybrid_quick_sort(arr, pi+1, high, threshold)

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

# Test function
def run_sorting_algorithm(algorithm, data):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    if algorithm == "insertion_sort":
        insertion_sort(data)
    elif algorithm == "quick_sort":
        quick_sort(data, 0, len(data)-1)
    elif algorithm == "hybrid_quick_sort":
        hybrid_quick_sort(data, 0, len(data)-1)
    print("Comparisons:", comparisons, "Swaps:", swaps)
    return data

def test_algorithm(algorithm_name, data_generator, n):
    print(f"Testing {algorithm_name} with {data_generator.__name__} data, n={n}")
    data = data_generator(n)
    if n < 40:  # Wypisywanie danych wejściowych dla n < 40
        print("Input data:", data)
    sorted_data = run_sorting_algorithm(algorithm_name, data.copy())
    if n < 40:  # Wypisywanie posortowanych danych dla n < 40
        print("Sorted data:", sorted_data)
    print("Is sorted:", sorted_data == sorted(data))
    print("---")

# Main testing routine
if __name__ == "__main__":
    for algorithm in ["insertion_sort", "quick_sort", "hybrid_quick_sort"]:
        for data_generator in [generate_random_keys, generate_ascending_keys, generate_descending_keys]:
            for n in [8, 32]:
                test_algorithm(algorithm, data_generator, n)
