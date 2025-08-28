"""
Basic implementation of HashMap with collision mechanism implementend with linked lists
"""

from src.linked_list import Node, LinkedList


class HashMapLinkedList(LinkedList[tuple[str, int]]):
    def __init__(self) -> None:
        self._head: Node[tuple[str, int]] | None = None

    def find(self, key: str) -> int:
        ret = None
        node = self._head
        while node is not None:
            if node.value[0] == key:
                ret = node.value[1]
            node = node.next

        if not ret:
            raise KeyError(f"Item with key: {key} not found!")

        return ret


class HashMap:
    HASH_SIZE = 10

    def __init__(self, hash_size: int = HASH_SIZE) -> None:
        self._hash_map: list[HashMapLinkedList | None] = [None] * hash_size

    def __setitem__(self, key: str, value: int) -> None:
        hash_ = self.get_hash(key)
        if not self._hash_map[hash_]:
            self._hash_map[hash_] = HashMapLinkedList()
        self._hash_map[hash_].add_head((key, value))

    def __getitem__(self, key: str) -> int:
        hash_ = self.get_hash(key)
        ll = self._hash_map[hash_]
        if not ll:
            raise KeyError(f"Value with key: {key}, does not exist!")
        ret = ll.find(key)
        return ret

    def get_hash(self, key: str) -> int:
        return sum(map(ord, key)) % 10
