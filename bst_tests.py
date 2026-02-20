import math
import random
import sys
import unittest
from dataclasses import dataclass
from bst import delete, insert, lookup, BinarySearchTree, Node, equal
import random

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
            insert(tree, elem)

        for elem in ["Z", "A", "D", "B"]:
            self.assertTrue(lookup(tree, elem))
            delete(tree, elem)
            self.assertFalse(lookup(tree, elem))

    def test_point(self):
        @dataclass(frozen=True)
        class P:
            x: int
            y: int

            def distance(self) -> float:
                return math.sqrt(self.x ** 2 + self.y ** 2)

        def point_cmp(v1: P, v2: P) -> bool:
            return v1.distance() < v2.distance()

        self.assertTrue(point_cmp(P(0, 0), (P(1, 1))))
        self.assertFalse(point_cmp(P(1, 1), (P(0, 0))))
        self.assertTrue(equal(P(1, 1), (P(1, 1)), point_cmp))

        random.seed(0)

        def generatePoint() -> P:
            return P(random.randint(0, 10_000_000), random.randint(0, 10_000_000))

        tree = BinarySearchTree(None, point_cmp)
        points = [generatePoint() for _ in range(100)]

        for elem in points:
            insert(tree, elem)

        for elem in points:
            self.assertTrue(lookup(tree, elem))
            delete(tree, elem)
            self.assertFalse(lookup(tree, elem))

    def test_reverse_int(self):
        def reverse_cmp(v1: int, v2: int) -> bool:
            return v1 > v2

        self.assertTrue(reverse_cmp(1, 0))
        self.assertFalse(reverse_cmp(0, 1))
        self.assertTrue(equal(1, 1, reverse_cmp))

        random.seed(0)

        tree = BinarySearchTree(None, reverse_cmp)
        points = [random.randint(0, 10_000_000) for _ in range(100)]

        for elem in points:
            insert(tree, elem)

        for elem in points:
            self.assertTrue(lookup(tree, elem))
            delete(tree, elem)
            self.assertFalse(lookup(tree, elem))


if __name__ == '__main__':
    unittest.main()
