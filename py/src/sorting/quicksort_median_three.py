"""Quicksort implementation with pivot picked by median of three. Hoare's partitioning"""


def partition(arr: list[int], left: int, r: int) -> int:  # type: ignore[return]
    i = left
    j = r
    pivot = arr[r]
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def partition_median(arr: list[int], left: int, r: int) -> int:
    mid = (left + r) // 2
    if arr[mid] < arr[left]:
        arr[mid], arr[left] = arr[left], arr[mid]
    if arr[r] < arr[left]:
        arr[left], arr[r] = arr[r], arr[left]
    if arr[mid] < arr[r]:
        arr[mid], arr[r] = arr[r], arr[mid]
    return partition(arr, left, r)


def quicksort(
    arr: list[int], left: int = 0, r: int | None = None
) -> list[int]:
    if r is None:
        r = len(arr) - 1
    if left >= r:
        return []

    p = partition_median(arr, left, r)
    quicksort(arr, left, p)
    quicksort(arr, p + 1, r)
    return arr
