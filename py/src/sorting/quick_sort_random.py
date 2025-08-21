"""Quicksort implementation with pivot picked randomly. Lomuto partition"""
import random


def partition(arr: list[int], l: int, r: int) -> int:
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def partition_rand(arr: list[int], l: int, r: int) -> int:
    rand = random.randint(l, r)
    arr[rand], arr[r] = arr[r], arr[rand]
    return partition(arr, l, r)


def quicksort(arr: list[int], l: int = 0, r: int | None = None) -> list[int]:
    if r is None:
        r = len(arr) - 1
    if l >= r:
        return []

    p = partition_rand(arr, l, r)
    quicksort(arr, l, p - 1)
    quicksort(arr, p + 1, r)
    return arr
