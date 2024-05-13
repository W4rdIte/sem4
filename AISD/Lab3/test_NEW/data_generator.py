import random
import sys


def generate_random_array(n):
    return [random.randint(0, 2 * n - 1) for _ in range(n)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    n = int(sys.argv[1])

    random_array = generate_random_array(n)
    print(" ".join(map(str, random_array)))
