import sys

comparisons = 0
swaps = 0
output_file = "sort_c&s.txt"


def insertion_sort(arr, low, high):
    global comparisons, swaps
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
        if j >= low:
            comparisons += 1
        if len(arr) < 40:
            print("Insertion Sort Swap:", arr)


def quick_sort(arr, low, high, threshold):
    global comparisons, swaps
    if low < high:
        if high - low + 1 <= threshold:
            insertion_sort(arr, low, high)
        else:
            pivot = partition(arr, low, high)
            quick_sort(arr, low, pivot - 1, threshold)
            quick_sort(arr, pivot + 1, high, threshold)


def partition(arr, low, high):
    global comparisons, swaps
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    if len(arr) < 40:
        print("Quick Sort Swap:", arr)
    return i + 1


def hybrid_sort(arr, threshold=10):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    quick_sort(arr, 0, len(arr) - 1, threshold)
    return comparisons, swaps


def print_array(arr):
    print(" ".join(map(str, arr)))


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python hybrid_sort.py")
        sys.exit(1)

    with open(output_file, "a") as file:
        for line in sys.stdin:
            arr = list(map(int, line.split()))
            print("HYBRID_SORT: ", len(arr))
            print("Original Array:")
            print_array(arr)
            comparisons, swaps = hybrid_sort(arr)
            print("Comparisons:", comparisons, "- Swaps:", swaps)
            print("Sorted Array:")
            print_array(arr)
            print("Is sorted:", is_sorted(arr))
            print()

            file.write(f"h {len(arr)} {comparisons} {swaps}\n")
