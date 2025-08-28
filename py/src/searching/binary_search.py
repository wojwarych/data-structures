def binary_search(
    arr: list[int], value: int, start: int = 0, end: int | None = None
) -> int | None:
    if end is None:
        end = len(arr) - 1
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] == value:
        return arr[mid]
    if arr[mid] > value:
        return binary_search(arr, value, start, mid - 1)
    return binary_search(arr, value, mid + 1, end)
