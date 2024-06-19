import select

# from select import select
# from randomized_select import randomized_select
# from binary_search import binary_search


def randomized_select(arr, left, right, i, comparisons, swaps):
    import random

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


def binary_search(arr, left, right, v, comparisons):
    if left <= right:
        mid = left + (right - left) // 2

        comparisons[0] += 1
        if arr[mid] == v:
            return 1

        comparisons[0] += 1
        if arr[mid] < v:
            return binary_search(arr, mid + 1, right, v, comparisons)
        return binary_search(arr, left, mid - 1, v, comparisons)
    return 0


def test_selection_algorithms():
    vec = [2, 7, 12, 8, 3, 2, 4, 4, 4, 1, 12, 10]
    expected_results = [1, 2, 2, 3, 4, 4, 4, 7, 8, 10, 12, 12]
    comparisons = [0]
    swaps = [0]
    for i in range(len(vec)):
        vec_copy = vec[:]
        assert (
            randomized_select(vec_copy, 0, len(vec) - 1, i + 1, comparisons, swaps)
            == expected_results[i]
        )
    print("Randomized Select Tests Passed!")

    comparisons = [0]
    swaps = [0]
    for i in range(len(vec)):
        vec_copy = vec[:]
        assert (
            select(vec_copy, 0, len(vec) - 1, i + 1, comparisons, swaps)
            == expected_results[i]
        )
    print("Select Tests Passed!")


def test_binary_search():
    vec = [1, 3, 4, 5, 7, 10]
    comparisons = [0]
    assert binary_search(vec, 0, len(vec) - 1, 0, comparisons) == 0
    assert binary_search(vec, 0, len(vec) - 1, 1, comparisons) == 1
    assert binary_search(vec, 0, len(vec) - 1, 2, comparisons) == 0
    assert binary_search(vec, 0, len(vec) - 1, 3, comparisons) == 1
    assert binary_search(vec, 0, len(vec) - 1, 4, comparisons) == 1
    assert binary_search(vec, 0, len(vec) - 1, 5, comparisons) == 1
    assert binary_search(vec, 0, len(vec) - 1, 6, comparisons) == 0
    assert binary_search(vec, 0, len(vec) - 1, 7, comparisons) == 1
    assert binary_search(vec, 0, len(vec) - 1, 8, comparisons) == 0
    assert binary_search(vec, 0, len(vec) - 1, 9, comparisons) == 0
    assert binary_search(vec, 0, len(vec) - 1, 10, comparisons) == 1
    assert binary_search(vec, 0, len(vec) - 1, 11, comparisons) == 0
    print("Binary Search Tests Passed!")


def main():
    test_selection_algorithms()
    test_binary_search()


if __name__ == "__main__":
    main()
