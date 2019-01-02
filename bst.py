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
        if self.root == None:
            return None

        return self.__search(self.root, value)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return self.root

        return self.__insert(self.root, value)

    def traverse(self, mode):
        if self.root == None:
            return None

        values = []
        unvisited = Queue()
        unvisited.put(self.root)

        self.__level_order(values, unvisited)

        return values

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

    def __search(self, node, value):
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
            if node.left == None:
                node.left = Node(value)
                return node.left
            else:
                return self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = Node(value)
                return node.right
            else:
                return self.__insert(node.right, value)
