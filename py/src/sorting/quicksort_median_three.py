"""Quicksort implementation with pivot picked by median of three. Hoare's partitioning"""
import random
import statistics
import time


def partition(arr: list[int], l: int, r: int) -> int:
    i = l
    j = r
    pivot = arr[l]
    while i < j:
        while arr[i] <= pivot and i < j:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def partition_median(arr: list[int], l: int, r: int) -> int:
    m = statistics.median([arr[l], arr[r], arr[(r-l) // 2]])
    idx = arr.index(m)
    arr[idx], arr[l] = arr[r], arr[idx]
    return partition(arr, l, r)


def quicksort(arr: list[int], l: int, r: int) -> list[int]:
    if l >= r:
        return

    p = partition_median(arr, l, r)
    quicksort(arr, l, p - 1)
    quicksort(arr, p + 1, r)
    return arr


if __name__ == "__main__":
    s = time.time()
    R = range(100)
    arr = [random.choice(R) for _ in range(10000)]
    print(quicksort(arr, 0, len(arr) - 1))
    e = time.time() - s
    print(e)
