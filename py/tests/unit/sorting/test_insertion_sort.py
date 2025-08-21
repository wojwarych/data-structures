from src.sorting.insertion_sort import insertion_sort


def test_insertion_sort_sorts_unordered_list() -> None:
    input_list = [3, 9, 10, 6, 1, -1, 7]
    assert insertion_sort(input_list) == sorted(input_list)


def test_insertion_sort_sorts_empty_list() -> None:
    input_list: list[int] = []
    assert insertion_sort(input_list) == input_list


def test_insertion_sort_keeps_sorted_list_sorted() -> None:
    input_list = sorted([3, 9, 10, 6, 1, -1, 7])
    assert insertion_sort(input_list) == input_list


def test_insertion_sort_sorts_reversed_list() -> None:
    input_list = sorted([3, 9, 10, 6, 1, -1, 7])
    reversed_list = input_list[::-1]
    assert insertion_sort(input_list) == reversed_list[::-1]
