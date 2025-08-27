"""Quicksort implementation with pivot picked randomly. Lomuto partition"""

import random


def partition(arr: list[int], left: int, r: int) -> int:
    i = left - 1
    pivot = arr[r]
    for j in range(left, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def partition_rand(arr: list[int], left: int, r: int) -> int:
    rand = random.randint(left, r)
    arr[rand], arr[r] = arr[r], arr[rand]
    return partition(arr, left, r)


def quicksort(arr: list[int], left: int = 0, r: int | None = None) -> list[int]:
    if r is None:
        r = len(arr) - 1
    if left >= r:
        return []

    p = partition_rand(arr, left, r)
    quicksort(arr, left, p - 1)
    quicksort(arr, p + 1, r)
    return arr
