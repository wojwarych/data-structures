package stack

import (
	"errors"

	"github.com/warycwoj/data-structures/linkedlist"
)

type DynamicStack struct {
	top  *linkedlist.Node
	size int
}

// NewDynamicStack() returns pointer to newly created empty stack
func NewDynamicStack() *DynamicStack {
	return &DynamicStack{}
}

// Size() returns current size of stack
func (s DynamicStack) Size() int {
	return s.size
}

// IsEmpty() returns boolean which evaluates if stack's size is 0 or more
func (s DynamicStack) IsEmpty() bool {
	return s.size == 0
}

// Push() pushes new Node with int value to the top of stack
func (s *DynamicStack) Push(val int) error {
	n := &linkedlist.Node{}
	n.SetVal(val)
	if s.IsEmpty() {
		s.top = n
	} else {
		n.SetNext(s.top)
		s.top = n
	}
	s.size += 1
	return nil
}

// Pop() removes Node from top of stack and returns value it stored
func (s *DynamicStack) Pop() (int, error) {
	if s.IsEmpty() {
		return -1, &ErrorStack{Err: errors.New("Cannot pop item from stack"), Cause: " DynamicStack is empty!"}
	}
	data := s.top.Peek()
	s.top = s.top.GetNext()
	s.size -= 1
	return data, nil
}

// Peek() peeks value of top item in the stack
func (s DynamicStack) Peek() (int, error) {
	if s.top == nil {
		return -1, &ErrorStack{Err: errors.New("Cannot peek top item from stack!"), Cause: " DynamicStack is empty!"}
	}
	return s.top.Peek(), nil
}
