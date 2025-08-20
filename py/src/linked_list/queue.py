"""
Queue implementation in Python with usage of Doubly Linked List
"""

from doubly_linked_list import Node, DoublyLinkedList


class Queue:
    def __init__(self) -> None:
        self._dl = DoublyLinkedList()

    def enqueue(self, value: int) -> None:
        n = Node(value)
        self._dl.add_tail(n)

    def dequeue(self) -> int:
        return self._dl.remove_head().value

    def peek(self) -> int:
        return self._dl.head.value


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(200)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(10)
    print(queue.peek())
