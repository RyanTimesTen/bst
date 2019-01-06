from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        if other == None:
            return False
        return (self.value == other.value and
                self.left == other.left and
                self.right == other.right)

class BST:
    def __init__(self):
        self.root = None

    def search(self, value):
        if self.root is None:
            return None

        return self.__search(self.root, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return self.root

        return self.__insert(self.root, value)

    def traverse(self, mode='level_order'):
        if self.root is None:
            return None

        values = []

        if mode == 'level_order':
            unvisited = Queue()
            unvisited.put(self.root)

            self.__level_order(values, unvisited)
        elif mode == 'inorder':
            self.__inorder(self.root, values)
        elif mode == 'preorder':
            self.__preorder(self.root, values)
        elif mode == 'postorder':
            self.__postorder(self.root, values)

        return values

    def calculate_height(self):
        if self.root is None:
            return None

        return self.__calculate_depth_of_deepest_node(self.root)

    def __search(self, node, value):
        if node is None:
            return None

        if value == node.value:
            return node
        elif value < node.value:
            return self.__search(node.left, value)
        else:
            return self.__search(node.right, value)

    def __insert(self, node, value):
        if value == node.value:
            return None
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                return node.left
            else:
                return self.__insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                return node.right
            else:
                return self.__insert(node.right, value)

    def __level_order(self, values, unvisited):
        if unvisited.empty():
            return

        node = unvisited.get()
        values.append(node.value)

        if node.left:
            unvisited.put(node.left)
        if node.right:
            unvisited.put(node.right)

        self.__level_order(values, unvisited)

    def __inorder(self, node, values):
        if node.left:
            self.__inorder(node.left, values)
        values.append(node.value)
        if node.right:
            self.__inorder(node.right, values)

    def __preorder(self, node, values):
        values.append(node.value)
        if node.left:
            self.__preorder(node.left, values)
        if node.right:
            self.__preorder(node.right, values)

    def __postorder(self, node, values):
        if node.left:
            self.__postorder(node.left, values)
        if node.right:
            self.__postorder(node.right, values)
        values.append(node.value)

    def __calculate_depth_of_deepest_node(self, node):
        if self.__is_leaf(node):
            return 0
        elif node.left and node.right:
            return 1 + max(
                self.__calculate_depth_of_deepest_node(node.left),
                self.__calculate_depth_of_deepest_node(node.right))
        elif node.left:
            return 1 + self.__calculate_depth_of_deepest_node(node.left)
        else:
            return 1 + self.__calculate_depth_of_deepest_node(node.right)

    def __is_leaf(self, node):
        return node.left is None and node.right is None
