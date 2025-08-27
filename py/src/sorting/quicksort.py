"""Quicksort implementation with pivot picked as a last element. Lomuto partition"""

import random
import time


def partition(arr: list[int], left: int, r: int) -> int:
    i = left - 1
    pivot = arr[r]
    for j in range(left, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quicksort(arr: list[int], left: int = 0, r: int | None = None) -> list[int]:
    if r is None:
        r = len(arr) - 1
    if left >= r:
        return []

    p = partition(arr, left, r)
    quicksort(arr, left, p - 1)
    quicksort(arr, p + 1, r)
    return arr


if __name__ == "__main__":
    s = time.time()
    R = range(10000)
    arr = [random.choice(R) for _ in range(10000)]
    print(quicksort(arr))
    e = time.time() - s
    print(e)
