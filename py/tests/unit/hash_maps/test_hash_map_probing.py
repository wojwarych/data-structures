from src.hash_tables.hash_map_collision_probing import HashMap

import pytest


def test_hash_map_basic_setup() -> None:
    hm = HashMap()
    assert hm.HASH_SIZE == 10


def test_hash_map_get_hash() -> None:
    hm = HashMap()
    assert hm.get_hash("test") == sum(map(ord, "test")) % 10


def test_hash_map_set_item_get_item() -> None:
    hm = HashMap()

    hm["test"] = 10

    assert hm["test"] == 10


def test_hash_map_set_item_get_item_existing_hash() -> None:
    hm = HashMap()

    hm["test"] = 10
    hm["xtest"] = 22

    assert hm["xtest"] == 22


def test_hash_map_set_item_get_item_non_existing_key() -> None:
    hm = HashMap()

    with pytest.raises(KeyError):
        assert hm["xtest"]


def test_hash_map_set_item_get_item_non_existing_key_collision_scenario() -> None:
    hm = HashMap()
    hm["a"] = 33

    with pytest.raises(KeyError):
        assert hm["da"]


def test_hash_map_set_item_get_item_probing_goes_to_end_of_hash_array() -> None:
    hm = HashMap()

    hm["a"] = 33
    hm["da"] = 88
    hm["dda"] = 456

    assert hm["a"] == 33
    assert hm["da"] == 88
    assert hm["dda"] == 456


def test_hash_map_set_item_get_item_probing_goes_to_beginning_of_array() -> None:
    hm = HashMap()

    hm["c"] = 33
    hm["ec"] = 88
    hm["eea"] = 456

    assert hm["c"] == 33
    assert hm["ec"] == 88
    assert hm["eea"] == 456
