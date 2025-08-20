class Node:
    def __init__(self, value: int) -> None:
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self) -> int:
        return self._value

    @property
    def left(self) -> int:
        return self._left

    @left.setter
    def left(self, _left: "Node") -> None:
        self._left = _left

    @property
    def right(self) -> int:
        return self._right

    @right.setter
    def right(self, _right: "Node") -> int:
        self._right = _right

    def add_child(self, data: int) -> None:
        if data == self._value:
            return

        if data < self._value:
            if self._left:
                self._left.add_child(data)
            else:
                self._left = Node(data)
        else:
            if self._right:
                self._right.add_child(data)
            else:
                self._right = Node(data)

    def search(self, data):
        if self._value == data:
            return True

        if data < self._value:
            if self._left:
                return self._left.search(data)
            else:
                return False

        if data > self._value:
            if self._right:
                return self._right.search(data)
            else:
                return False

    def in_order_traversal(self) -> None:
        elements = []
        if self._left:
            elements += self._left.in_order_traversal()

        elements.append(self._value)

        if self._right:
            elements += self._right.in_order_traversal()

        return elements

    def find_min(self):
        if self._left is None:
            return self._value
        else:
            return self._left.find_min()

    def find_max(self):
        if self._right is None:
            return self._value
        else:
            return self._right.find_max()

    def delete(self, value):
        if value < self._value:
            if self._left:
                self._left = self._left.delete(value)
        elif value > self._value:
            if self._right:
                self._right = self._right.delete(value)
        else:
            if self._left is None and self._right is None:
                return None
            if self._left is None:
                return self._right
            if self._right is None:
                return self._left

            min_val = self._right.find_min()
            self._value = min_val
            self._right = self._right.delete(min_val)

        return self


def build_tree(elements):
    root = Node(elements[0])

    for i in elements:
        root.add_child(i)
    return root

if __name__ == "__main__":
    nums = [17, 2, 10, 99, 3, 5, -3, 24, 100]
    numbers_tree = build_tree(nums)
    numbers_tree.delete(100)
    print(numbers_tree.in_order_traversal())
