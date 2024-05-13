import random
import sys

from data_generator import generate_random_array
from utils import colors, test_run


def partition(arr, left, right, comparisons, swaps):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            swaps[0] += 1
            i += 1
        comparisons[0] += 1

    arr[i], arr[right] = arr[right], arr[i]
    swaps[0] += 1
    return i


def randomized_partition(arr, left, right, comparisons, swaps):
    n = right - left + 1
    random_pivot = random.randint(0, n - 1)
    arr[left + random_pivot], arr[right] = arr[right], arr[left + random_pivot]
    swaps[0] += 1
    return partition(arr, left, right, comparisons, swaps)


def randomized_select(arr, left, right, i, comparisons, swaps):
    if left == right:
        return arr[left]
    global_pivot_index = randomized_partition(arr, left, right, comparisons, swaps)
    local_pivot_index = global_pivot_index - left + 1
    if i == local_pivot_index:
        return arr[global_pivot_index]
    elif i < local_pivot_index:
        return randomized_select(
            arr, left, global_pivot_index - 1, i, comparisons, swaps
        )
    else:
        return randomized_select(
            arr,
            global_pivot_index + 1,
            right,
            i - local_pivot_index,
            comparisons,
            swaps,
        )


def main():
    comparisons = [0]
    swaps = [0]

    k = int(sys.argv[1])
    n = int(sys.argv[2])
    arr = generate_random_array(n)

    left = 0
    right = len(arr) - 1
    i = 5

    print("Original array:", arr)

    kth_smallest = randomized_select(arr, left, right, i, comparisons, swaps)

    print("Array after select:", arr)
    print(f"K = {k} -> {colors.RED} {kth_smallest} {colors.END}")
    print(f"Number of swaps: {swaps[0]}")
    print(f"Number of comparisons: {comparisons[0]}")

    with open(test_run.output_file, "a") as file:
        file.write(f"r {n} {comparisons[0]} {swaps[0]} {k}\n")


if __name__ == "__main__":
    main()
