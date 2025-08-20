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



def in_order_traversal(root_node: Node) -> list[str]:
    if root_node is None:
        return
    in_order_traversal(root_node.left)
    print(root_node.value)
    in_order_traversal(root_node.right)

def pre_order_traversal(root_node: Node) -> list[str]:
    if root_node is None:
        return
    print(root_node.value)
    pre_order_traversal(root_node.left)
    pre_order_traversal(root_node.right)

def post_order_traversal(root_node: Node) -> list[str]:
    if root_node is None:
        return
    post_order_traversal(root_node.left)
    post_order_traversal(root_node.right)
    print(root_node.value)


if __name__ == "__main__":
    r = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    r.left = b
    r.right = c
    b.left = d
    b.right = e
    c.right = f

    # in_order_traversal(r)
    # pre_order_traversal(r)
    post_order_traversal(r)
