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
    left: BinTree[T]
    right: BinTree[T]


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


def left_or_right(Target: T, bst: BinTree[T], comes_before: Callable[[T, T], bool])->BinTree[T]:
    if bst is None:
        return Node(Target, None, None)
    elif comes_before(Target, bst.value):
        return Node(bst.value, left_or_right(Target, bst.left, comes_before), bst.right)
    elif comes_before(bst.value, Target):
        return Node(bst.value, bst.left, left_or_right(Target, bst.right, comes_before))
    else: 
        return bst
    
# adds target value and returns new tree
def insert(bst: BinarySearchTree[T], Target: T) -> BinarySearchTree[T]:
    return BinarySearchTree(left_or_right(Target, bst.tree, bst.comes_before), bst.comes_before)


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
    return BinarySearchTree(delete_helper(bst.tree, target, bst.comes_before), bst.comes_before)


def delete_helper(tree: BinTree[T], target: T, comes_before: Callable[[T, T], bool]) -> BinTree[T]:
    if tree is None:
        return None
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
