import unittest

from bst import BST, Node

class TestBSTBase(unittest.TestCase):
    def setUp(self):
        self.subject = BST()

    def setup_full_tree(self):
        self.subject.root = Node(25)
        self.subject.root.left = Node(15)
        self.subject.root.right = Node(50)
        self.subject.root.left.left = Node(10)
        self.subject.root.left.right = Node(22)
        self.subject.root.left.left.left = Node(4)
        self.subject.root.left.left.right = Node(12)
        self.subject.root.left.right.left = Node(18)
        self.subject.root.left.right.right = Node(24)
        self.subject.root.right.left = Node(35)
        self.subject.root.right.right = Node(70)
        self.subject.root.right.left.left = Node(31)
        self.subject.root.right.left.right = Node(44)
        self.subject.root.right.right.left = Node(66)
        self.subject.root.right.right.right = Node(90)
