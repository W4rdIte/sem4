import sys

from data_generator import generate_random_array
from utils import colors

output_file = "sort_c&s.txt"
swaps = 0
comparisons = 0


def select(arr, k):
    """
    Find the k-th smallest element in the array using Median-finding Algorithm.

    Parameters:
    arr (list): The input list.
    k (int): The index of the element to be found (0-based).

    Returns:
    int: The k-th smallest element.
    """
    global swaps, comparisons
    if len(arr) == 1:
        return arr[0]

    pivot = median_of_medians(arr)

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]

    if k < len(left):
        comparisons += len(arr) - 1
        swaps += len(arr) - 1
        return select(left, k)
    elif k < len(left) + len(mid):
        comparisons += len(arr) - 1
        return mid[0]
    else:
        comparisons += len(arr) - 1
        swaps += len(arr) - 1
        return select(right, k - len(left) - len(mid))


def median_of_medians(arr, group_size=5):
    """
    Find the median of medians of the input array.

    Parameters:
    arr (list): The input list.
    group_size (int): The size of each group used for finding the median of medians.

    Returns:
    int: The median of medians.
    """
    global swaps, comparisons
    if len(arr) <= group_size:
        return sorted(arr)[len(arr) // 2]

    chunks = [arr[i : i + group_size] for i in range(0, len(arr), group_size)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    return select(medians, len(medians) // 2)


if __name__ == "__main__":
    k = int(sys.argv[1])
    n = int(sys.argv[2])  # Retrieve n from command line arguments
    

    arr = generate_random_array(n)
    sorted_arr = sorted(arr)

    result = select(arr, k - 1)

    # print(f"Random Array:", arr)
    # print(f"Sorted Array:", sorted_arr)
    print(f"K = {k} -> {colors.RED} {result} {colors.END}")
    # print(f"Number of swaps: {swaps}")
    # print(f"Number of comparisons: {comparisons}")

    with open(output_file, "a") as file:
        file.write(f"s {n} {comparisons} {swaps} {k}\n")
