import random
from SplayTree import SplayTree
from utils import colors


def test_case_1(n):
    print(
        f"{colors.PURPLE}Test Case 1: Insert increasing sequence and delete random sequence{colors.END}"
    )
    tree = SplayTree()
    keys = list(range(2 * n - 1))
    for key in keys:
        print(f"{colors.GREEN}Insert {key}{colors.END}")
        tree.insert(key)
        tree.print_tree()
        print()

    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]
    for key in keys:
        print(f"{colors.RED}Delete {key}{colors.END}")
        tree.delete(key)
        tree.print_tree()
        print()


def test_case_2(n):
    print(
        f"{colors.PURPLE}Test Case 2: Insert random sequence and delete random sequence{colors.END}"
    )
    tree = SplayTree()
    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]

    for key in keys:
        tree.insert(key)
        print(f"{colors.GREEN}Insert {key}{colors.END}")
        tree.print_tree()
        print()

    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]
    for key in keys:
        tree.delete(key)
        print(f"{colors.RED}Delete {key}{colors.END}")
        tree.print_tree()
        print()


# Run the test cases
n = 50
test_case_1(n)
test_case_2(n)
