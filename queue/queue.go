// package queue implements basic design of data structure called Queue (FIFO)

package queue

import (
	"fmt"

	"github.com/warycwoj/data-structures/linkedlist"
)

type Queue struct {
	head *linkedlist.Node
	tail *linkedlist.Node
	size int
}

// NewQueue() returns pointer to newly created empty Queue
func NewQueue() *Queue {
	return &Queue{}
}

// Size() returns current size of Queue
func (q Queue) Size() int {
	return q.size
}

// IsEmpty() returns boolean value fo whether Queue is empty or not
func (q Queue) IsEmpty() bool {
	return q.size == 0
}

// Enqueue() adds new Node at the head of the Queue and increases size of Queue
func (q *Queue) Enqueue(val int) {
	n := &linkedlist.Node{}
	n.SetVal(val)
	if q.IsEmpty() {
		q.head, q.tail = n, n
	} else {
		prevHead := q.head
		q.head = n
		prevHead.SetPrev(q.head)
		q.head.SetNext(prevHead)
	}
	q.size += 1
}

// Dequeue() removes first item that was added to the Queue structure
func (q *Queue) Dequeue() int {
	prevTail := q.tail
	data := prevTail.Peek()
	q.tail = prevTail.GetPrev()
	q.tail.SetNext(nil)
	return data
}

// String() implements Stringer interface
func (q Queue) String() string {
	var ret string
	for node := q.head; node != nil; {
		ret = ret + fmt.Sprintf("%d\n", node.Peek())
		node = node.GetNext()
	}
	return fmt.Sprintf("%s", ret)
}
