def linear_search(arr: list[int], item: int) -> int | None:
    for i in arr:
        if i == item:
            return i
    return None
