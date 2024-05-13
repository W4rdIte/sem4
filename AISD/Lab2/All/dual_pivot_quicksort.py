import sys

comparisons = 0
swaps = 0
output_file = "sort_c&s.txt"


def dualPivotQuickSort(arr, low, high):
    if low < high:
        lp, rp = partition(arr, low, high)

        dualPivotQuickSort(arr, low, lp - 1)
        dualPivotQuickSort(arr, lp + 1, rp - 1)
        dualPivotQuickSort(arr, rp + 1, high)

    return swaps, comparisons


def partition(arr, low, high):
    global swaps, comparisons

    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
        swaps += 1
        print("Swapped", arr[low], "and", arr[high])
        print("Array:", arr)

    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]

    while k <= g:
        comparisons += 1
        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
            swaps += 1
            print("Swapped", arr[k], "and", arr[j - 1])
            print("Array:", arr)
        elif arr[k] >= q:
            while arr[g] > q and k < g:
                g -= 1
                comparisons += 1

            arr[k], arr[g] = arr[g], arr[k]
            g -= 1
            if arr[k] < p:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1
                swaps += 1
                print("Swapped", arr[k], "and", arr[j - 1])
                print("Array:", arr)

        k += 1

    j -= 1
    g += 1

    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]
    swaps += 2
    print("Pivots placed:", arr[low], "and", arr[high])
    print("Array:", arr)

    return (
        j,
        g,
    )


def print_arr(arr):
    print(" ".join(map(str, arr)))


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python quick_sort.py")
        sys.exit(1)
    with open(output_file, "a") as file:
        for line in sys.stdin:
            arr = list(map(int, line.split()))
            print("DUAL_PIVOT_QUICK_SORT: ", len(arr))
            print("Original arr:")
            print_arr(arr)
            swaps = comparisons = 0
            dualPivotQuickSort(arr, 0, len(arr) - 1)
            print("Sorted arr:")
            print_arr(arr)
            print("Swaps:", swaps)
            print("Comparisons:", comparisons)
            print("Is sorted:", is_sorted(arr))
            print()

            file.write(f"d {len(arr)} {comparisons} {swaps}\n")
