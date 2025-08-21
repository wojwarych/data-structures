from src.hash_tables.hash_map_collision import HashMap

import pytest


@pytest.fixture
def hash_map() -> HashMap:
    return HashMap()


def test_hash_map_init(hash_map: HashMap) -> None:
    assert hash_map.HASH_SIZE == 10


def test_hash_map_set_value_get_value_returns_correct_value(hash_map: HashMap) -> None:
    value = 33
    hash_map["test"] = value

    assert hash_map["test"] == value


def test_hash_map_set_value_get_value_returns_correct_value_next_in_chain(hash_map: HashMap) -> None:
    first_val = 33
    second_val = 234
    hash_map["test"] = first_val
    hash_map["xtest"] = second_val

    assert hash_map["test"] == first_val


def test_hash_map_raises_key_error_when_key_not_found(hash_map: HashMap) -> None:
    value = 33
    hash_map["test"] = value

    with pytest.raises(KeyError):
        hash_map["random"]


def test_hash_map_raises_key_error_when_key_not_found_same_hash(hash_map: HashMap) -> None:
    value = 33
    hash_map["test"] = value

    with pytest.raises(KeyError):
        hash_map["xtest"]


def test_hash_map_get_hash(hash_map: HashMap) -> None:
    assert hash_map.get_hash("foo") == sum(map(ord, "foo")) % 10
