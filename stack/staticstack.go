// package stack implements basic types of stack: static and dynamic stack and their minimal interfaces on top of LinkedList ADT

package stack

import (
	"errors"
	"fmt"

	"github.com/warycwoj/data-structures/linkedlist"
)

type StaticStack struct {
	top     *linkedlist.Node
	size    int
	maxSize int
}

// NewStack() returns pointer to newly created empty stack with set max size of stack
func NewStaticStack(maxSize int) *StaticStack {
	return &StaticStack{maxSize: maxSize}
}

// Size() returns current size of stack
func (ss StaticStack) Size() int {
	return ss.size
}

// IsEmpty() returns boolean evaluating if size of stack is 0 or more
func (ss *StaticStack) IsEmpty() bool {
	return ss.size == 0
}

// Push() pushes new item to the top of the stack if its max size is not reached
// Else returns an ErrorStack error
func (ss *StaticStack) Push(val int) error {
	if ss.size == ss.maxSize {
		return &ErrorStack{
			Err:   errors.New("Cannot push new item to the stack!"),
			Cause: fmt.Sprintf(" Stack reached it's max size of %d!", ss.maxSize),
		}
	}
	n := &linkedlist.Node{}
	n.SetVal(val)
	if ss.IsEmpty() {
		ss.top = n
	} else {
		n.SetNext(ss.top)
		ss.top = n
	}
	ss.size += 1
	return nil
}

// Pop() removes item form top of stack and returns its value
func (ss *StaticStack) Pop() (int, error) {
	if ss.IsEmpty() {
		return -1, &ErrorStack{Err: errors.New("Cannot pop item from stack"), Cause: " DynamicStack is empty!"}
	}
	data := ss.top.Peek()
	ss.top = ss.top.GetNext()
	ss.size -= 1
	return data, nil
}
