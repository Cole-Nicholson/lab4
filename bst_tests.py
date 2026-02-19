import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10 ** 9)
from bst import delete, insert, lookup, BinarySearchTree, Node


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
        val = delete(
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

        self.assertEqual(
            val,
            BinarySearchTree(
                Node(
                    "A",
                    None,
                    None
                ),
                str_cmp
            ),
        )


if __name__ == '__main__':
    unittest.main()
