import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import time

from bst import BinarySearchTree, insert, delete, lookup, BinTree

sys.setrecursionlimit(10 ** 9)

TREES_PER_RUN: int = 10 ** 4


def float_cmp(a: float, b: float) -> bool:
    return a < b


def random_tree(n: int) -> BinarySearchTree[float]:
    tree = BinarySearchTree(None, float_cmp)
    for _ in range(n):
        tree = insert(tree, random.random())

    return tree


SAMPLE_COUNT = 50


# Generates a list of SAMPLE_COUNT integer values between 0 and the given max_value inclusive
def sample_values(max_value: int) -> List[int]:
    stepSize: float = max_value / SAMPLE_COUNT

    return [int(round(stepSize * n)) for n in range(1, SAMPLE_COUNT + 1)]


def height(tree: BinTree[float]) -> int:
    if tree is None:
        return 0

    return 1 + max(height(tree.left), height(tree.right))


n_max = 50
# startTime = time.perf_counter()
#
# trees = [random_tree(n_max) for _ in range(TREES_PER_RUN)]
#
# print(f"Generated in {time.perf_counter() - startTime}s")
#
# print(height(trees[0].tree))
#
# xs = []
# ys = []
#
# for sample_size in sample_values(n_max):
#     trees = [random_tree(sample_size) for _ in range(TREES_PER_RUN)]
#     heights = [height(tree.tree) for tree in trees]
#     ys.append(sum(heights) / len(heights))
#     xs.append(sample_size)

xs2 = []
ys2 = []
for sample_size in sample_values(n_max):
    trees = [random_tree(sample_size) for _ in range(TREES_PER_RUN)]
    times = []
    for tree in trees:
        start_time = time.perf_counter_ns()
        insert(tree, random.random())
        runtime = time.perf_counter_ns() - start_time
        times.append(runtime)
    ys2.append(sum(times) / len(times))
    xs2.append(sample_size)
    print(xs2)
    print(ys2)


def make_graph(x_coords: List[float], y_coords: List[float]) -> None:
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy: np.ndarray = np.array(x_coords)
    y_numpy: np.ndarray = np.array(y_coords)
    plt.plot(x_numpy, y_numpy, label='Time')
    plt.xlabel("X (Number of elements)")
    plt.ylabel("Y (ns)")
    plt.title("Time to insert into trees with different element counts")
    plt.grid(True)
    plt.legend()  # makes the 'label's show up
    plt.show()


if __name__ == '__main__':
    make_graph(xs2, ys2)
