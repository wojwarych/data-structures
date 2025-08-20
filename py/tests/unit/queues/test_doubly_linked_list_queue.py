from src.queues.queue import Queue


def test_queue_enqueue_dequeue_returns_same_value() -> None:
    inp = 4
    queue = Queue(inp)

    queue.enqueue(4)

    assert queue.peek() == inp
    assert queue.dequeue() == inp
