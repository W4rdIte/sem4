import random
import sys

from data_generator import generate_random_array
from utils import colors


output_file = "sort_c&s.txt"
swaps = 0
comparisons = 0


def randomized_select(arr, k):
    global swaps, comparisons
    if len(arr) == 1:
        return arr[0]

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]

    if k < len(left):
        comparisons += len(arr) - 1
        swaps += len(arr) - 1
        return randomized_select(left, k)
    elif k < len(left) + len(mid):
        comparisons += len(arr) - 1
        return mid[0]
    else:
        comparisons += len(arr) - 1
        swaps += len(arr) - 1
        k -= len(left) + len(mid)
        return randomized_select(right, k)


if __name__ == "__main__":
    k = int(sys.argv[1])
    n = int(sys.argv[2])

    arr = generate_random_array(n)
    sorted_arr = sorted(arr)

    result = randomized_select(arr, k - 1)

    # print(f"Random Array:", arr)
    # print(f"Sorted Array:", sorted_arr)
    print(f"K = {k} -> {colors.RED} {result} {colors.END}")
    # print(f"Number of swaps: {swaps}")
    # print(f"Number of comparisons: {comparisons}")

    with open(output_file, "a") as file:
        file.write(f"r {n} {comparisons} {swaps} {k}\n")
