import random
import sys


def generate_random_array(n):
    return [random.randint(0, 2 * n - 1) for _ in range(n)]


def generate_sorted_array(n):
    return list(range(n))


def generate_reverse_sorted_array(n):
    return list(range(n - 1, -1, -1))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data_generator.py <array_length>")
        sys.exit(1)

    n = int(sys.argv[1])

    random_array = generate_random_array(n)
    print(" ".join(map(str, random_array)))

    sorted_array = generate_sorted_array(n)
    print(" ".join(map(str, sorted_array)))

    reverse_sorted_array = generate_reverse_sorted_array(n)
    print(" ".join(map(str, reverse_sorted_array)))
