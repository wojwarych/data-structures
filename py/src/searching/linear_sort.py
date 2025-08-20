def find(arr: list[int], item: int) -> int | None:
    for i in arr:
         if i == item:
             return i
    return None


if __name__ == "__main__":
    arr = [5, 10, 9, 11, 0, 8]
    print(find(arr, 11))
