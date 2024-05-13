import sys
from data_generator import generate_random_array
from utils import colors, test_run


def quick_sort_partition(arr, left, right, comparisons, swaps):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        comparisons[0] += 1
        swaps[0] += 1

    arr[i], arr[right] = arr[right], arr[i]
    swaps[0] += 1
    return i


def quick_sort(arr, left, right, comparisons, swaps):
    if left >= right:
        return

    pivot_index = quick_sort_partition(arr, left, right, comparisons, swaps)
    quick_sort(arr, left, pivot_index - 1, comparisons, swaps)
    quick_sort(arr, pivot_index + 1, right, comparisons, swaps)


def find_median(arr, left, right, comparisons, swaps):
    quick_sort(arr, left, right, comparisons, swaps)
    return arr[left + (right - left) // 2]


def partition(arr, left, right, pivot, comparisons, swaps):
    i = left
    for j in range(left, right):
        comparisons[0] += 1
        if arr[j] == pivot:
            break
    arr[i], arr[right] = arr[right], arr[i]
    swaps[0] += 1

    i = left
    for j in range(left, right):
        comparisons[0] += 1
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            swaps[0] += 1
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    swaps[0] += 1
    return i


def select(arr, left, right, k, comparisons, swaps, medians_array_size):
    n = right - left + 1
    medians = [
        (n + medians_array_size - 1) // medians_array_size
        for _ in range((n + medians_array_size - 1) // medians_array_size)
    ]
    i = 0
    while i < n // medians_array_size:
        medians[i] = find_median(
            arr,
            left + i * medians_array_size,
            left + i * medians_array_size + medians_array_size - 1,
            comparisons,
            swaps,
        )
        i += 1
    if i * medians_array_size < n:
        medians[i] = find_median(
            arr,
            left + i * medians_array_size,
            left + i * medians_array_size + (n % medians_array_size - 1),
            comparisons,
            swaps,
        )
        i += 1

    median_of_medians = (
        medians[0]
        if i == 1
        else select(medians, 0, i - 1, i // 2, comparisons, swaps, medians_array_size)
    )

    pivot_index = partition(arr, left, right, median_of_medians, comparisons, swaps)
    i = pivot_index - left + 1
    if i == k:
        return arr[pivot_index]
    elif i > k:
        return select(
            arr, left, pivot_index - 1, k, comparisons, swaps, medians_array_size
        )
    else:
        return select(
            arr, pivot_index + 1, right, k - i, comparisons, swaps, medians_array_size
        )


def main():
    comparisons = [0]
    swaps = [0]

    k = int(sys.argv[1])
    n = int(sys.argv[2])
    medians_array_size = int(sys.argv[3])

    arr = generate_random_array(n)

    # print("Original array:", arr)

    kth_smallest = select(
        arr, 0, len(arr) - 1, k, comparisons, swaps, medians_array_size
    )

    print("Array after select:", arr)
    print(f"K = {k} -> {colors.RED} {kth_smallest} {colors.END}")
    print(f"Number of swaps: {swaps[0]}")
    print(f"Number of comparisons: {comparisons[0]}")

    with open(test_run.output_file, "a") as file:
        file.write(
            f"s {n} {comparisons[0]} {swaps[0]} {k} {test_run.medians_array_size}\n"
        )


if __name__ == "__main__":
    main()
