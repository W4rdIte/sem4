import sys


output_file = "sort_c&s.txt"


def merge_sort(arr):
    comparisons = 0
    swaps = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        _, comparisons_left, swaps_left = merge_sort(left_half)
        _, comparisons_right, swaps_right = merge_sort(right_half)

        comparisons += comparisons_left + comparisons_right
        swaps += swaps_left + swaps_right

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            comparisons += 1
            swaps += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            swaps += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            swaps += 1

    return arr, comparisons, swaps


def read_array_from_file(filename):
    with open(filename, "r") as file:
        array = list(map(int, file.readline().strip().split()))
    return array


# Example usage
if __name__ == "__main__":
    input_lines = sys.stdin.readlines()

    with open(output_file, "a") as file:
        for line in input_lines:
            arr = list(map(int, line.strip().split()))
            print("Przed sortowaniem:", arr)
            sorted_arr, comparisons, swaps = merge_sort(arr.copy())
            print("Po sortowaniu:", sorted_arr)
            print("Liczba porównań:", comparisons)
            print("Liczba zamian:", swaps)
            print()
            file.write(f"m {len(arr)} {comparisons} {swaps}\n")
