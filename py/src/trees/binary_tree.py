from collections import deque


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


def depth_first_traversal(root_node: Node) -> list[int]:
    stack = []
    stack.append(root_node)

    ret = []

    while stack:
        val = stack.pop()
        ret.append(val.value)
        if val.right:
            stack.append(val.right)
        if val.left:
            stack.append(val.left)

    return ret


def depth_first_traversal_recursive(root_node: Node) -> list[int]:
    if not root_node:
        return []
    return (
        [
            root_node.value,
        ]
        + depth_first_traversal_recursive(root_node.left)
        + depth_first_traversal_recursive(root_node.right)
    )


def breadth_first_traversal(root_node: Node) -> list[int]:
    ret = []
    dq = deque()
    dq.appendleft(root_node)

    while dq:
        val = dq.pop()
        ret.append(val.value)
        if val.left:
            dq.appendleft(val.left)
        if val.right:
            dq.appendleft(val.right)
    return ret


def breadth_first_find(root_node: Node, find: str) -> bool:
    dq = deque()
    dq.appendleft(root_node)

    while dq:
        val = dq.pop()
        if val.value == find:
            return True
        if val.left:
            dq.appendleft(val.left)
        if val.right:
            dq.appendleft(val.right)
    return False


def depth_first_find_recursive(root_node: Node, find: str) -> bool:
    if root_node is None:
        return False
    elif root_node.value == find:
        return True
    return depth_first_find_recursive(
        root_node.left, find
    ) or depth_first_find_recursive(root_node.right, find)


def depth_first_sum_recursive(root_node: Node) -> int:
    if root_node is None:
        return 0
    return (
        root_node.value
        + depth_first_sum_recursive(root_node.left)
        + depth_first_sum_recursive(root_node.right)
    )


def depth_first_min_value_iteratively(root_node: Node) -> int:
    stack = []
    stack.append(root_node)
    current = float("inf")
    while stack:
        node = stack.pop()
        if node.value < current:
            current = node.value
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return current


def depth_first_min_value_recursively(root_node: Node) -> int:
    if root_node is None:
        return float("inf")
    left_val = depth_first_min_value_recursively(root_node.left)
    right_val = depth_first_min_value_recursively(root_node.right)
    node_val = root_node.value
    return min([node_val, left_val, right_val])


def depth_first_max_root_to_leaf_path(root_node: Node) -> int:
    if root_node is None:
        return float("-inf")
    if not root_node.left and not root_node.right:
        return root_node.value
    left_val = depth_first_max_root_to_leaf_path(root_node.left)
    right_val = depth_first_max_root_to_leaf_path(root_node.right)
    print(left_val, right_val)
    val = left_val if left_val > right_val else right_val
    return root_node.value + val


r = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)
r.left = b
r.right = c
b.left = d
b.right = e
c.right = f

print(depth_first_traversal(r))
print(depth_first_traversal_recursive(r))
print(breadth_first_traversal(r))
print(breadth_first_find(r, "j"))
print(depth_first_find_recursive(r, "j"))
print(depth_first_sum_recursive(r))
print(depth_first_min_value_iteratively(r))
print(depth_first_min_value_recursively(r))
print()
print(depth_first_max_root_to_leaf_path(r))
