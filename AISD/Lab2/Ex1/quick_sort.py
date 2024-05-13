import sys

comparisons = 0
swaps = 0


def quick_sort(arr):
    global comparisons, swaps
    comparisons = 0
    swaps = 0

    def partition(arr, low, high):
        global comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i = i + 1
                (arr[i], arr[j]) = (arr[j], arr[i])
                swaps += 1
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
        swaps += 1
        if len(arr) < 40:
            print("Swap:", swaps, "- arr:", arr)
        return i + 1

    def quick_sort_helper(arr, low, high):
        global comparisons, swaps
        if low < high:
            split_index = partition(arr, low, high)
            quick_sort_helper(arr, low, split_index - 1)
            quick_sort_helper(arr, split_index + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    print("Number of comparisons:", comparisons)
    print("Number of swaps:", swaps)
    return comparisons, swaps


def print_arr(arr):
    print(" ".join(map(str, arr)))


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python quick_sort.py")
        sys.exit(1)

    for line in sys.stdin:
        arr = list(map(int, line.split()))
        print("QUICK_SORT: ", len(arr))
        print("Original arr:")
        print_arr(arr)
        quick_sort(arr)
        print("Sorted arr:")
        print_arr(arr)
        print("Is sorted:", is_sorted(arr))
        print()
