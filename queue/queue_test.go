package queue

import "testing"

func TestNewQueue(t *testing.T) {
	q := NewQueue()
	if q.head != nil {
		t.Errorf("New empty Queue failed to initialize! Head is not nil!")
	}
	if q.tail != nil {
		t.Errorf("New empty Queue failed to initialize! Tail is not nil!")
	}
	if q.size != 0 {
		t.Errorf("New empty Queue failed to initialize! Size is not 0!")
	}
}

func TestEnqueue(t *testing.T) {
	q := NewQueue()
	for _, v := range []int{1, 4, 8, 99, 103, 55} {
		q.Enqueue(v)
	}
	if q.head.Peek() != 55 || q.tail.Peek() != 1 {
		t.Errorf("Enqueue() did not add values to the Queue correctly!")
	}
}

func TestDequeue(t *testing.T) {
	q := NewQueue()
	for _, v := range []int{1, 4, 8, 99, 103, 55} {
		q.Enqueue(v)
	}
	ret := q.Dequeue()
	if q.head.Peek() != 55 || q.tail.Peek() != 4 || ret != 1 {
		t.Errorf("Dequeue() did not removed value from the Queue correctly!")
	}
}
