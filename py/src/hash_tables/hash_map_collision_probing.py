"""
Basic implementation of HashMap with collision mechanism implementend with linear probing
"""


class HashMap:
    HASH_SIZE = 10

    def __init__(self, hash_size: int = HASH_SIZE) -> None:
        self._hash_map: list[tuple[str, int] | None] = [None] * hash_size

    def __setitem__(self, key: str, value: int) -> None:
        hash_ = self.get_hash(key)
        if not self._hash_map[hash_]:
            self._hash_map[hash_] = (key, value)
        else:
            start_hash = hash_ + 1
            while start_hash < len(self._hash_map):
                if not self._hash_map[start_hash]:
                    self._hash_map[start_hash] = (key, value)
                    return
                start_hash += 1
            start_hash = 0
            while start_hash < hash_:
                if not self._hash_map[start_hash]:
                    self._hash_map[start_hash] = (key, value)
                    return
                start_hash += 1

    def __getitem__(self, key: str) -> int:
        hash_ = self.get_hash(key)
        if self._hash_map[hash_] and self._hash_map[hash_][0] == key:
            return self._hash_map[hash_][1]
        else:
            start_hash = hash_ + 1
            while start_hash < len(self._hash_map):
                if (
                    self._hash_map[start_hash]
                    and self._hash_map[start_hash][0] == key
                ):
                    return self._hash_map[start_hash][1]
                start_hash += 1

            start_hash = 0
            while start_hash < hash_:
                if (
                    self._hash_map[start_hash]
                    and self._hash_map[start_hash][0] == key
                ):
                    return self._hash_map[start_hash][1]
                start_hash += 1
        raise KeyError(f"Value with key: {key} not found!")

    def get_hash(self, key: str) -> int:
        return sum(map(ord, key)) % 10
