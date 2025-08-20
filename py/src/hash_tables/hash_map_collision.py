"""
Basic implementation of HashMap with collision mechanism implementend with linked lists
"""


class Node:
    def __init__(self, value: tuple[str, int]) -> None:
        self._value = value
        self._next = None

    @property
    def next(self) -> "Node | None":
        return self._next

    @next.setter
    def next(self, node: "Node") -> None:
        self._next = node

    @property
    def value(self) -> tuple[str, int]:
        return self._value

    @value.setter
    def value(self, value: tuple[str, int]) -> None:
        self._value = value


class LinkedList:
    def __init__(self) -> None:
        self._head = None

    def add(self, value: tuple[str, int]) -> None:
        new_node = Node(value)
        if not self._head:
            self._head = new_node
            return None

        last_node = self._head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def find(self, key: str) -> int | None:
        node = self._head
        while node is not None:
            if node.value[0] == key:
                return node.value[1]
            node = node.next
        return None


class HashMap:
    def __init__(self, hash_size: int  = 10) -> None:
        self._hash_map: list[LinkedList | None] = [None] * hash_size

    def __setitem__(self, key: str, value: tuple[str, int]) -> None:
        hash_ = self.get_hash(key)
        if not self._hash_map[hash_]:
            self._hash_map[hash_] = LinkedList()
        self._hash_map[hash_].add((key, value))

    def __getitem__(self, key: str) -> int:
        hash_ = self.get_hash(key)
        ll = self._hash_map[hash_]
        if not ll:
            raise KeyError(f"Value with key: {key}, does not exist!")
        ret = ll.find(key)
        if not ret:
            raise KeyError(f"Value with key: {key}, does not exist!")

    def get_hash(self, key: str) -> int:
        return sum(map(ord, key)) % 10



if __name__ == "__main__":
    hm = HashMap()

    hm["foo"] = 10
    hm["dfoo"] = 55
    hm["test key"] = 666
    print(hm["ddfoo"])
