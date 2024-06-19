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
