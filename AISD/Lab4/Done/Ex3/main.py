import random
from RBTree import RBTree
from utils import colors


def test_case_1(n):
    print(
        f"{colors.PURPLE}Test Case 1: Insert increasing sequence and delete random sequence{colors.END}"
    )

    tree = RBTree()
    keys = list(range(2 * n - 1))

    for key in keys:
        print(f"{colors.GREEN}insert {key}{colors.END}")
        tree.insertNode(key)
        tree.print_tree()
        print()

    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]
    for key in keys:
        print(f"{colors.RED}delete {key}{colors.END}")
        tree.delete_node(key)
        tree.print_tree()
        print()


def test_case_2(n):
    print(
        f"{colors.PURPLE}Test Case 2: Insert random sequence and delete random sequence{colors.END}"
    )

    tree = RBTree()
    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]

    for key in keys:
        print(f"{colors.GREEN}insert {key}{colors.END}")
        tree.insertNode(key)
        tree.print_tree()
        print()

    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]
    for key in keys:
        print(f"{colors.RED}delete {key}{colors.END}")
        tree.delete_node(key)
        tree.print_tree()
        print()


# Run the test cases
n = 50
test_case_1(n)
test_case_2(n)
