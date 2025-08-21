from collections.abc import Callable

import pytest

from src.sorting.quicksort import quicksort
from src.sorting.quick_sort_random import quicksort as quicksort_random
from src.sorting.quicksort_median_three import quicksort as quicksort_median_three


@pytest.mark.parametrize("method", [quicksort, quicksort_random, quicksort_median_three])
def test_quicksort_method_sorts_unordered_list(method: Callable) -> None:
    input_list = [3, 9, 10, 6, 1, -1, 7]
    assert method(input_list) == sorted(input_list)


@pytest.mark.parametrize("method", [quicksort, quicksort_random, quicksort_median_three])
def test_quicksort_method_sorts_empty_list(method: Callable) -> None:
    input_list: list[int] = []
    assert method(input_list) == input_list


@pytest.mark.parametrize("method", [quicksort, quicksort_random, quicksort_median_three])
def test_quicksort_method_keeps_sorted_list_sorted(method: Callable) -> None:
    input_list = sorted([3, 9, 10, 6, 1, -1, 7])
    assert method(input_list) == input_list


@pytest.mark.parametrize("method", [quicksort, quicksort_random, quicksort_median_three])
def test_quicksort_method_sorts_reversed_list(method: Callable) -> None:
    input_list = sorted([3, 9, 10, 6, 1, -1, 7])
    reversed_list = input_list[::-1]
    assert method(input_list) == reversed_list[::-1]
