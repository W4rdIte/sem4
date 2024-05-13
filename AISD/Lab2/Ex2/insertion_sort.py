import sys


comparisons = 0
swaps = 0
output_file = "sort_c&s.txt"


def insertion_sort(arr):
    global comparisons, swaps
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1], arr[j] = arr[j], key
            swaps += 1
            j -= 1
            if len(arr) < 40:
                print("Swap:", swaps, "- Array:", arr)
        arr[j + 1] = key
        if j >= 0:
            comparisons += 1

    return comparisons, swaps


def print_array(arr):
    print(" ".join(map(str, arr)))


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python insertion_sort.py")
        sys.exit(1)

    with open(output_file, "a") as file:
        for line in sys.stdin:
            arr = list(map(int, line.split()))
            print("INSERTION_SORT: ", len(arr))
            print("Original Array:")
            print_array(arr)
            comparisons, swaps = insertion_sort(arr)
            print("Comparisons:", comparisons, "- Swaps:", swaps)
            print("Sorted Array:")
            print_array(arr)
            print("Is sorted:", is_sorted(arr))
            print()

            file.write(f"i {len(arr)} {comparisons} {swaps}\n")
