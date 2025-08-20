"""Implementation of general tree with usage of Nodes and Linked Lists"""
class LinkedList:
    def __init__(self) -> None:
        self._head = None

    def add(self, node: "TreeNode") -> None:
        if not self._head:
            self._head = node
            return
        prev_head = self._head
        while prev_head._next:
            prev_head = prev_head._next
        prev_head._next = node

    def iterate(self):
        node = self._head
        while node:
            yield node
            node = node._next


class TreeNode:
    def __init__(self, value: int) -> None:
        self._parent = None
        self._value = value
        self._next = None
        self._children = LinkedList()

    def print_tree(self) -> None:
        print(self._value)
        if self._children._head:
            for child in self._children.iterate():
                child.print_tree()

    def add_child(self, node: "TreeNode") -> None:
        self._children.add(node)



if __name__ == "__main__":
    root = TreeNode("foo")

    bar = TreeNode("bar")
    baz = TreeNode("baz")
    bar.add_child(baz)
    stupd = TreeNode("stupd")
    baz.add_child(stupd)

    xyz = TreeNode("xyz")

    root.add_child(xyz)
    root.add_child(bar)
    root.print_tree()
