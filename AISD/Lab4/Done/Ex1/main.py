import random
from BST import BST
from utils import colors


def test_case_1(n):
    print(
        f"{colors.PURPLE}Case 1: Inserting increasing sequence and deleting random sequence{colors.END}"
    )

    tree = BST()
    keys = list(range(2 * n - 1))

    for key in keys:
        tree.insert(key)

    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]

    for key in keys:
        tree.delete(key)


def test_case_2(n):
    print(
        f"{colors.PURPLE}Case 2: Inserting random sequence and deleting random sequence{colors.END}"
    )

    tree = BST()
    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]

    for key in keys:
        tree.insert(key)

    keys = [random.randint(0, 2 * n - 1) for _ in range(n)]
    for key in keys:
        tree.delete(key)


# Run the test cases
n = 50
test_case_1(n)
test_case_2(n)
