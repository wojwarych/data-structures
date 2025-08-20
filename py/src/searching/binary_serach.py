def binary_search(arr: list[int], value: int) -> int | None:
    mid = len(arr) // 2
    if arr[mid] == value:
        return arr[mid]
    elif arr[mid] > value:
        return binary_search(arr[:mid], value)
    elif arr[mid] < value:
        return binary_search(arr[mid:], value)
    else:
        return None


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 6, 7, 8, 9, 11]
    print(binary_search(arr, 5))
