// Package linkedlist implement basic examples of data structure called Linked List

package linkedlist

import (
	"errors"
	"fmt"
)

// SingleLinkedList is struct implementing singly linked list
type SingleLinkedList struct {
	head *Node
	size int
}

func NewSingleLinkedList() SingleLinkedList {
	return SingleLinkedList{nil, 0}
}

// GetHead() returns pointer to the head of SingleLinkedList
func (ll SingleLinkedList) GetHead() *Node {
	return ll.head
}

// Size() return size of SingleLinkedList
func (ll SingleLinkedList) Size() int {
	return ll.size
}

// IsEmpty() returns boolean whetehr list is empty or not
func (ll SingleLinkedList) IsEmpty() bool {
	return ll.size == 0
}

// Add() adds new Node with integer value to the list
func (ll *SingleLinkedList) Add(val int) {
	if ll.IsEmpty() {
		ll.AddFirst(val)
	} else {
		ll.AddLast(val)
	}
}

// AddFirst() adds new Node with integer value at the beginning of the list
func (ll *SingleLinkedList) AddFirst(val int) {
	newHead := &Node{val: val}
	if ll.IsEmpty() {
		ll.head = newHead
	} else {
		prevHead := ll.head
		newHead.next = prevHead
		ll.head = newHead
	}
	ll.size += 1
}

// AddLast() adds new Node with integer value at the end of the list
func (ll *SingleLinkedList) AddLast(val int) {
	node := ll.head.next
	prev := ll.head
	for node != nil {
		prev = node
		node = node.next
	}
	n := &Node{val: val}
	prev.next = n
	ll.size += 1
}

// AddAt() adds new Node with integer value at desired index
// If index is out of bounds of list it returns an false value with error
func (ll *SingleLinkedList) AddAt(idx, val int) (bool, error) {
	if idx > ll.size || idx < 0 {
		return false, &ErrLinkedList{Err: errors.New("Index out of list bounds!")}
	}
	if idx == 0 {
		ll.AddFirst(val)
		return true, nil
	}
	prev := ll.head
	for i, node := 0, ll.head; node != nil; i++ {
		if idx == i {
			newNode := &Node{val: val, next: node}
			prev.next = newNode
			ll.size += 1
			return true, nil
		}
		prev = node
		node = node.next
	}
	return false, nil
}

// String() iterates over nodes of list and formats them
func (ll SingleLinkedList) String() string {
	var ret string
	for i, node := 0, ll.head; node != nil; i++ {
		ret = ret + fmt.Sprintf("%d: %d\n", i, node.Peek())
		node = node.next
	}
	return fmt.Sprintf("%s", ret)
}

// Get() returns value of Node on desired index if index is in bounds of list
func (ll SingleLinkedList) Get(idx int) (ret int, err error) {
	if idx > ll.size || idx < 0 {
		return -1, &ErrLinkedList{Err: errors.New("Index out of list bounds!")}
	}
	node := ll.head
	for i := 0; node != nil; i++ {
		if i == idx {
			return node.Peek(), nil
		}
		node = node.next
	}
	return -1, err
}

// Set() updates value of a Node on a desired index if index is in bounds of list
func (ll *SingleLinkedList) Set(idx, val int) (ret int, err error) {
	if idx > ll.size || idx < 0 {
		return -1, &ErrLinkedList{Err: errors.New("Index out of list bounds!")}
	}
	for i, node := 0, ll.head; node != nil; i++ {
		if i == idx {
			node.SetVal(val)
			return node.Peek(), nil
		}
		node = node.next
	}
	return -1, errors.New("Undefined error!")
}

// IndexOf() returns index of searched value
// It returns -1 if value does not exist in list
func (ll SingleLinkedList) IndexOf(val int) int {
	for node, i := ll.head, 0; node != nil; i++ {
		if node.Peek() == val {
			return i
		}
		node = node.next
	}
	return -1
}

// PeekFirst() returns value of head Node of list if list is not empty
func (ll SingleLinkedList) PeekFirst() (int, error) {
	if ll.IsEmpty() {
		return -1, &ErrLinkedList{errors.New("Empty list!"), " No value to show!"}
	}
	return ll.head.Peek(), nil
}

// RemoveFirst() removes head Node of list and sets new Node if list is not empty
func (ll *SingleLinkedList) RemoveFirst() (int, error) {
	if ll.IsEmpty() {
		return -1, &ErrLinkedList{errors.New("List is empty!"), " Cannot delete any value!"}
	}
	data := ll.head.Peek()
	ll.head = ll.head.next
	ll.size -= 1
	return data, nil
}

// RemoveLast() removes last Node of list if it is not empty
func (ll *SingleLinkedList) RemoveLast() (int, error) {
	if ll.IsEmpty() {
		return -1, &ErrLinkedList{errors.New("List is empty!"), " Cannot delete any value!"}
	}
	node := ll.head
	prev := node
	for node.next != nil {
		prev = node
		node = node.next
	}
	data := node.Peek()
	prev.next = nil
	ll.size -= 1
	return data, nil
}

// Clear() deletes all Nodes from list
func (ll *SingleLinkedList) Clear() {
	for node := ll.head; node != nil; {
		node = node.next
		ll.head = node
	}
	ll.size = 0
}
