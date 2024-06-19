from Node import Node


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return self.splay(node, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_right_subtree = self.find_min(node.right)
                node.key = min_right_subtree.key
                node.right = self._delete(node.right, min_right_subtree.key)
        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def splay(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            if node.left is None:
                return node
            if key < node.left.key:
                node.left.left = self.splay(node.left.left, key)
                node = self.rotate_right(node)
            elif key > node.left.key:
                node.left.right = self.splay(node.left.right, key)
                if node.left.right is not None:
                    node.left = self.rotate_left(node.left)
            if node.left is not None:
                return self.rotate_right(node)
            else:
                return node
        else:
            if node.right is None:
                return node
            if key < node.right.key:
                node.right.left = self.splay(node.right.left, key)
                if node.right.left is not None:
                    node.right = self.rotate_right(node.right)
            elif key > node.right.key:
                node.right.right = self.splay(node.right.right, key)
                node = self.rotate_left(node)
            if node.right is not None:
                return self.rotate_left(node)
            else:
                return node

    def rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp

    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

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
