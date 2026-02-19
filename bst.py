import sys
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
    if bst.tree is None:
        return False

    if equal(bst.tree.value, target, bst.comes_before):
        return True

    if bst.comes_before(bst.tree.value, target):
        return lookup(BinarySearchTree(bst.tree.right, bst.comes_before), target)
    else:
        return lookup(BinarySearchTree(bst.tree.left, bst.comes_before), target)


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


def tree_max(tree: Node[T], comes_before: Callable[[T, T], bool]) -> T:
    if tree is None:
        return None
    if tree.right.value is not None:
        return tree_max(tree.right, comes_before)

    return tree.value


def tree_without(tree: BinTree[T], target: T, comes_before: Callable[[T, T], bool]) -> BinTree[T]:
    if tree is None:
        return None

    if equal(tree.value, target, comes_before):
        return None

    if comes_before(tree.value, target):
        return Node(
            tree.value,
            tree_without(
                tree.left,
                target, comes_before),
            tree.right
        )
    else:
        return Node(
            tree.value,
            tree.left,
            tree_without(
                tree.right, target, comes_before)
        )


def delete(bst: BinarySearchTree[T], target: T) -> BinarySearchTree[T]:
    # delete — given a BinarySearchTree and a value as arguments, remove
    # the value from the tree (if present) while preserving the binary search tree
    # property that, for a given node’s value, the values in the left subtree come before
    # and the values in the right subtree do not. If the tree happens to have multiple
    # nodes containing the value to be removed, only a single such node will be
    # removed.
    # This function returns the resulting BinarySearchTree.
    return BinarySearchTree(delete_helper(bst.tree, target, bst.comes_before), bst.comes_before)


def delete_helper(tree: BinTree[T], target: T, comes_before: Callable[[T, T], bool]) -> BinTree[T]:
    # if equal(tree.value, target, bst.comes_before):
    #     max_val = tree_max(BinarySearchTree(bst.tree.left, bst.comes_before))
    #     if max_val is None:
    #         return BinarySearchTree(Node(bst.tree.value, None, bst.tree.right), bst.comes_before)
    #     without = tree_without(bst, max_val)
    #     return BinarySearchTree(Node(max_val, without.tree.left, without.tree.right), bst.comes_before)
    #
    # if bst.comes_before(bst.tree.value, target):
    #     if bst.tree.right is None:
    #         return None
    #     return delete(BinarySearchTree(bst.tree.right, bst.comes_before), target)
    # else:
    #     return delete(BinarySearchTree(bst.tree.left, bst.comes_before), target)
    # pass

    if equal(tree.value, target, comes_before):
        if tree.left is None:
            return tree_without(tree.right, target, comes_before)
        elif tree.right is None:
            return tree_without(tree.left, target, comes_before)
        else:
            max_val = tree_max(tree.left, comes_before)
            if max_val is None:
                # Left tree is empty
                return tree_without(tree, max_val, comes_before)
            return Node(max_val, tree_without(tree.left, max_val, comes_before), tree.right)

    if comes_before(tree.value, target):
        if tree.right is None:
            return None
        return Node(tree.value, tree.left, delete_helper(tree.right, target, comes_before))
    else:
        if tree.left is None:
            return None
        return Node(tree.value, delete_helper(tree.left, target, comes_before), tree.right)
