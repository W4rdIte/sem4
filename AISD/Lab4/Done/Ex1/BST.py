from Node import Node
from utils import colors


class BST:

    def __init__(self):
        self.root = None
        self.insert_counter = 0

    def insert(self, key):
        print(f"{colors.GREEN}insert {key}{colors.END}")
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
        self.insert_counter += 1
        if self.insert_counter == 10:
            self.print_tree()
        else:
            self.print_tree()

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        print(f"{colors.RED}delete {key}{colors.END}")
        self.root = self._delete(self.root, key)
        self.print_tree()

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __printCall(self, node, indent, last):
        if node is not None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            print(f"{node.key}")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    def print_tree(self):
        self.__printCall(self.root, "", True)
