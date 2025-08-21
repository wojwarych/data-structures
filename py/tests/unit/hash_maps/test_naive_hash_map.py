from src.hash_tables.character_hashing import CharacterNaiveHashMap

import pytest


@pytest.fixture
def a_string() -> str:
    return "teststring"


def test_char_naive_hash_map(a_string: str) -> None:
    cnhm = CharacterNaiveHashMap(a_string)

    assert cnhm.is_in("r")


def test_char_naive_hash_map_char_not_in_string(a_string: str) -> None:
    cnhm = CharacterNaiveHashMap(a_string)

    assert not cnhm.is_in("x")


def test_char_naive_hash_map_char_outside_ascii_raises_type_error() -> None:
    string = "zażółćgęśląjaźń"
    with pytest.raises(TypeError):
        cnhm = CharacterNaiveHashMap(string)


def test_add_char_to_existing_hash_map(a_string: str) -> None:
    cnhm = CharacterNaiveHashMap(a_string)

    cnhm.add("x")

    assert cnhm.is_in("x")


def test_add_char_to_existing_hash_map_outside_ascii(a_string: str) -> None:
    cnhm = CharacterNaiveHashMap(a_string)

    with pytest.raises(TypeError):
        cnhm.add("ż")
