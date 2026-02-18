import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10 ** 9)

# ---- Data types ----
# Doing this with generics is more fun and technically safer than just `Any`
T = TypeVar("T")

# I don't know if there's a way to do this with traditional type aliases
type BinTree[T] = Node[T] | None


@dataclass(frozen=True)
class Node(Generic[T]):
    value: Any
    left: BinTree
    right: BinTree


@dataclass(frozen=True)
class BinarySearchTree(Generic[T]):
    tree: BinTree[T]
    comes_before: Callable[[T, T], bool]


# ---- Functions ----
example: BinarySearchTree[int] = BinarySearchTree(Node(10, None, None), lambda x, y: x < y)

print(example.tree)


# Returns whether two values are equal according to the `comes_before` function
def equal(a: T, b: T, comes_before: Callable[[T, T], bool]) -> bool:
    if not comes_before(a, b) and not comes_before(b, a):
        return True

    return False


# Find if a `value` is in a given `tree`
def lookup(bst: BinarySearchTree[T], target: T) -> bool:
    if bst.tree is not None:
        if equal(bst.tree.value, target, bst.comes_before):
            return True

    return max(
        equal(bst.tree.right.value, target, bst.comes_before) if bst.tree.right is not None else False,
        lookup(BinarySearchTree(bst.tree.left, bst.comes_before), target) if bst.tree.left is not None else False,
        lookup(BinarySearchTree(bst.tree.right, bst.comes_before), target) if bst.tree.right is not None else False
    )


def insert(tree: BinarySearchTree[T], value: T) -> BinarySearchTree[T]:
    # insert — given a BinarySearchTree and a value as arguments, add the
    # value to the tree by using the comes_before attribute to determine which
    # path to take at each node; insert into the left subtree if the value "comes before"
    # the value stored in the current node and into the right subtree otherwise. Again,
    # you should write a helper function that does all the recursive work using
    # BinTree. This helper function needs to accept the comes_before field of
    # BinarySearchTree as another argument.
    # This function returns the resulting BinarySearchTree.
    # Make sure to avoid inserting duplicate values!
    pass


def delete(tree: BinarySearchTree[T], value: T) -> BinarySearchTree[T]:
    # delete — given a BinarySearchTree and a value as arguments, remove
    # the value from the tree (if present) while preserving the binary search tree
    # property that, for a given node’s value, the values in the left subtree come before
    # and the values in the right subtree do not. If the tree happens to have multiple
    # nodes containing the value to be removed, only a single such node will be
    # removed.
    # This function returns the resulting BinarySearchTree.

    pass
