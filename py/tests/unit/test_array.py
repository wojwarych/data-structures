from src.array import DynamicArray

import pytest


@pytest.fixture
def pre_populated_da() -> DynamicArray:
    da = DynamicArray()

    for i in range(10):
        da.add(i)

    return da


def test_dynamic_array() -> None:
    da = DynamicArray()

    assert da.capacity == 0
    assert da.length == 0
    assert da.GROWTH_FACTOR == 1.5


def test_dynamic_array_add_data() -> None:
    da = DynamicArray()

    da.add(3)

    assert da.capacity == 1
    assert da.length == 1


def test_dynamic_array_add_data_over_bigger_arr(pre_populated_da: DynamicArray) -> None:
    pre_populated_da.add(80)

    assert pre_populated_da.length == 11
    assert pre_populated_da.capacity >= pre_populated_da.length


def test_dynamic_array_remove_raises_value_error_on_empty_array() -> None:
    da = DynamicArray()

    with pytest.raises(ValueError):
        da.remove()

def test_dynamic_array_remove_removes_last_item() -> None:
    da = DynamicArray()
    da.add(3)
    da.add(44)
    da.add(23)

    ret = da.remove()

    assert ret == 23


def test_dynamic_array_remove_at_raises_value_error_on_empty_array() -> None:
    da = DynamicArray()

    with pytest.raises(ValueError):
        da.remove_at()


def test_dynamic_array_remove_at_specific_index_empty_array() -> None:
    da = DynamicArray()

    with pytest.raises(IndexError):
        da.remove_at(3)


def test_dynamic_array_remove_at_specific_index_removes_data() -> None:
    da = DynamicArray()

    da.add(1)
    da.add(2)
    da.add(33)
    da.add(23)
    da.add(-1)

    ret = da.remove_at(2)

    assert ret == 2
    assert da.capacity >= da.length
    assert da.length == 4
    assert da.get(2) == 33


def test_dynamic_array_get_at_position() -> None:
    da = DynamicArray()
    da.add(44)

    assert da.get(1) == 44
