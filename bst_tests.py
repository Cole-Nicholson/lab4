import math
import sys
import unittest
from dataclasses import dataclass
from bst import delete, insert, lookup, BinarySearchTree, Node, equal
import random

from bst_graphs import height

sys.setrecursionlimit(10 ** 9)


class BSTTests(unittest.TestCase):
    def test_str(self):
        def str_cmp(v1: str, v2: str) -> bool:
            return v1 < v2

        self.assertTrue(str_cmp("Apple", "Banana"))
        self.assertTrue(not str_cmp("Hello World", "A"))
        self.assertFalse(lookup(BinarySearchTree(None, str_cmp), "Hello world"))
        self.assertFalse(lookup(BinarySearchTree(Node("A", None, None), str_cmp), "Hello world"))
        self.assertTrue(lookup(BinarySearchTree(Node("Banana", Node("A", None, None), None), str_cmp), "A"))
        self.assertTrue(
            lookup(
                BinarySearchTree(
                    Node(
                        "A",
                        None,
                        Node(
                            "Hello World", None, None
                        )
                    ),
                    str_cmp
                ),
                "Hello World"
            )
        )

        tree = BinarySearchTree(None, str_cmp)
        for elem in ["A", "Z", "D", "B"]:
            tree = insert(tree, elem)

        for elem in ["Z", "A", "D", "B"]:
            self.assertTrue(lookup(tree, elem), f"Failed on {elem}")
            tree = delete(tree, elem)
            self.assertFalse(lookup(tree, elem), f"Failed on {elem}")

    def test_point(self):
        @dataclass(frozen=True)
        class Point2D:
            x: int
            y: int

            def distance(self) -> float:
                return math.sqrt(self.x ** 2 + self.y ** 2)

        def point_cmp(v1: Point2D, v2: Point2D) -> bool:
            return v1.distance() < v2.distance()

        self.assertTrue(point_cmp(Point2D(0, 0), (Point2D(1, 1))))
        self.assertFalse(point_cmp(Point2D(1, 1), (Point2D(0, 0))))
        self.assertTrue(equal(Point2D(1, 1), (Point2D(1, 1)), point_cmp))

        random.seed(0)

        def generatePoint() -> Point2D:
            return Point2D(random.randint(0, 10_000_000), random.randint(0, 10_000_000))

        tree = BinarySearchTree(None, point_cmp)
        points = [generatePoint() for _ in range(100)]

        for elem in points:
            tree = insert(tree, elem)

        for elem in points:
            self.assertTrue(lookup(tree, elem), f"Failed on {elem}")
            tree = delete(tree, elem)
            self.assertFalse(lookup(tree, elem), f"Failed on {elem}")

    def test_reverse_int(self):
        def reverse_cmp(v1: int, v2: int) -> bool:
            return v1 > v2

        self.assertTrue(reverse_cmp(1, 0))
        self.assertFalse(reverse_cmp(0, 1))
        self.assertTrue(equal(1, 1, reverse_cmp))

        random.seed(0)

        tree = BinarySearchTree(None, reverse_cmp)
        points = [i for i in range(100)]
        random.shuffle(points)

        for elem in points:
            tree = insert(tree, elem)

        for elem in points:
            self.assertTrue(lookup(tree, elem), f"Failed on {elem}")
            tree = delete(tree, elem)
            self.assertFalse(lookup(tree, elem), f"Failed on {elem}")

    def test_insert(self):
        # Test worse case of a tree insert
        tree = BinarySearchTree[int](None, lambda a, b: a < b)
        for i in range(100):
            tree = insert(tree, i)
        self.assertTrue(height(tree.tree) == 100)

        l = list(range(100))
        random.shuffle(l)

        for idx,i in enumerate(l, start=1):
            tree = delete(tree, i)
            self.assertTrue(height(tree.tree) == 100-idx, f"Failed on {idx}")


if __name__ == '__main__':
    unittest.main()
