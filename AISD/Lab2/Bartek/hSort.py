def hybrid_quick_sort(arr, low, high, threshold=10):
    global comparisons, swaps
    if low < high:
        if high - low < threshold:
            insertion_sort_part(arr, low, high)
        else:
            pi = partition(arr, low, high)
            hybrid_quick_sort(arr, low, pi - 1, threshold)
            hybrid_quick_sort(arr, pi + 1, high, threshold)


def insertion_sort_part(arr, low, high):
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


def partition(arr, low, high):
    global comparisons, swaps
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    return i + 1
