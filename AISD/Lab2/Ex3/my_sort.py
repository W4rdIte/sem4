import sys

output_file = "sort_c&s.txt"


def merge(left, right):

    merged = []
    left_index, right_index = 0, 0
    comparisons = 0
    swaps = 0

    while left_index < len(left) and right_index < len(right):
        comparisons += 1
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            swaps += len(left) - left_index

    # Dołącz pozostałe elementy z lewej i prawej listy
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged, comparisons, swaps


def divide_and_conquer(arr, indent=""):
    """
    Algorytm Dziel i Zwyciężaj dzielący listę na spójne podciągi rosnące.
    """
    print(indent + "Dzielenie:", arr)
    if len(arr) <= 1:
        return [arr], 0, 0

    mid = len(arr) // 2
    left, comparisons_left, swaps_left = divide_and_conquer(arr[:mid], indent + "  ")
    right, comparisons_right, swaps_right = divide_and_conquer(arr[mid:], indent + "  ")

    merged, comparisons_merge, swaps_merge = merge(left[0], right[0])
    comparisons = comparisons_left + comparisons_right + comparisons_merge
    swaps = swaps_left + swaps_right + swaps_merge

    return [merged], comparisons, swaps


def CSSort(arr):

    # Dzielimy na spójne podciągi rosnące
    subsequences, comparisons, swaps = divide_and_conquer(arr)

    # Sortujemy spójne podciągi
    sorted_subsequences = [sorted(subsequence) for subsequence in subsequences]

    # Scalanie posortowanych podciągów
    sorted_arr = sorted_subsequences[0]
    for subsequence in sorted_subsequences[1:]:
        merged, comparisons_merge, swaps_merge = merge(sorted_arr, subsequence)
        comparisons += comparisons_merge
        swaps += swaps_merge
        sorted_arr = merged

    return sorted_arr, comparisons, swaps


if __name__ == "__main__":

    input_lines = sys.stdin.readlines()

    with open(output_file, "a") as file:
        for line in input_lines:
            arr = list(map(int, line.strip().split()))
            print("Tablica wejściowa:", arr)
            sorted_arr, comparisons, swaps = CSSort(arr)
            print("Posortowana tablica:", sorted_arr)
            print("Liczba porównań:", comparisons)
            print("Liczba permutacji:", swaps)
            print()
            file.write(f"y {len(arr)} {comparisons} {swaps}\n")
