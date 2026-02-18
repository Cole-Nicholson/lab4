import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10 ** 9)

# ---- Data types ----
T = TypeVar("T")

BinTree: TypeAlias = Optional["Node"[T]]


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
test: BinarySearchTree[int] = BinarySearchTree(Node(10, None, None), lambda x, y: x < y)
