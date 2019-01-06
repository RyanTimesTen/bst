import unittest

from bst import BST, Node
from .test_bst_base import TestBSTBase

class TestBSTInsert(TestBSTBase):
    def test_null(self):
        result = self.subject.insert(100)

        self.assertIsNotNone(self.subject.root)
        self.assertEqual(self.subject.root, result)

    def test_duplicate_at_root(self):
        self.subject.insert(100)

        result = self.subject.insert(100)

        self.assertIsNone(result)

    def test_duplicate(self):
        self.subject.insert(100)
        self.subject.insert(200)

        result = self.subject.insert(200)

        self.assertIsNone(result)

    def test_left(self):
        self.subject.insert(100)

        result = self.subject.insert(99)

        self.assertIsNotNone(self.subject.root.left)
        self.assertEqual(self.subject.root.left, result)
    
    def test_right(self):
        self.subject.insert(100)

        result = self.subject.insert(101)

        self.assertIsNotNone(self.subject.root.right)
        self.assertEqual(self.subject.root.right, result)

    def test_left_subtree(self):
        self.subject.insert(100)
        self.subject.insert(90)

        result = self.subject.insert(80)

        left_subtree = self.subject.root.left
        self.assertIsNotNone(left_subtree.left)
        self.assertEqual(left_subtree.left, result)

    def test_right_subtree(self):
        self.subject.insert(100)
        self.subject.insert(110)

        result = self.subject.insert(120)

        right_subtree = self.subject.root.right
        self.assertIsNotNone(right_subtree.right)
        self.assertEqual(right_subtree.right, result)

class TestBSTSearch(TestBSTBase):
    def test_null(self):
        result = self.subject.search(100)

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(100)

        result = self.subject.search(100)

        self.assertEqual(Node(100), result)

    def test_left(self):
        self.subject.root = Node(100)
        self.subject.root.left = Node(50)

        result = self.subject.search(50)

        self.assertEqual(Node(50), result)

    def test_right(self):
        self.subject.root = Node(100)
        self.subject.root.right = Node(150)

        result = self.subject.search(150)

        self.assertEqual(Node(150), result)
    
    def test_left_subtree(self):
        self.subject.root = Node(100)
        self.subject.root.left = Node(75)
        self.subject.root.left.left = Node(50)

        result = self.subject.search(50)

        self.assertEqual(Node(50), result)

    def test_right_subtree(self):
        self.subject.root = Node(100)
        self.subject.root.right = Node(125)
        self.subject.root.right.right = Node(150)

        result = self.subject.search(150)

        self.assertEqual(Node(150), result)

class TestBSTTreeHeight(TestBSTBase):
    def test_null(self):
        result = self.subject.calculate_height()

        self.assertIsNone(result)

    def test_root(self):
        self.subject.root = Node(5)

        result = self.subject.calculate_height()

        self.assertEqual(0, result)

    def test_height_small(self):
        self.subject.root = Node(6)
        self.subject.root.left = Node(4)
        self.subject.root.right = Node(100)
        self.subject.root.left.left = Node(2)
        self.subject.root.left.right = Node(5)
        self.subject.root.right.left = Node(8)
        self.subject.root.right.left.left = Node(7)

        result = self.subject.calculate_height()

        self.assertEqual(3, result)

    def test_height_one(self):
        self.subject.root = Node(5)
        self.subject.root.right = Node(8)

        result = self.subject.calculate_height()

        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
