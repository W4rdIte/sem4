from Node import Node


class BST:
    def __init__(self):
        self.root = None
        self.insert_counter = 0
        self.comparison_count = 0
        self.pointer_ops_count = 0
        self.heights = []

    def insert(self, key):
        self.comparison_count = 0
        self.pointer_ops_count = 0
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
        self.insert_counter += 1
        self.heights.append(self.get_height(self.root))

    def _insert(self, node, key):
        self.comparison_count += 1
        if key < node.key:
            self.pointer_ops_count += 1
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            self.pointer_ops_count += 1
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.comparison_count = 0
        self.pointer_ops_count = 0
        self.root = self._delete(self.root, key)
        self.heights.append(self.get_height(self.root))

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            self.comparison_count += 1
            node.left = self._delete(node.left, key)
        elif key > node.key:
            self.comparison_count += 1
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

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_metrics(self):
        return {
            "comparisons": self.comparison_count,
            "pointer_ops": self.pointer_ops_count,
            "height": max(self.heights),
        }
