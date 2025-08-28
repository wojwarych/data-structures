from collections.abc import Callable

from src.searching.binary_search import binary_search
from src.searching.linear_search import linear_search

import pytest


@pytest.fixture
def list_input() -> list[int]:
    return sorted([3, 99, 1, 11, 100, -5, -33])


@pytest.mark.parametrize("method", [binary_search, linear_search])
def test_binary_search_returns_correct_item(
    method: Callable, list_input: list[int]
) -> None:
    assert method(list_input, 99) == 99


@pytest.mark.parametrize("method", [binary_search, linear_search])
def test_binary_search_returns_correct_item_low_value(
    method: Callable, list_input: list[int]
) -> None:
    assert method(list_input, -5) == -5


@pytest.mark.parametrize("method", [binary_search, linear_search])
def test_binary_search_returns_no_item(
    method: Callable, list_input: list[int]
) -> None:
    assert not method(list_input, 900)
