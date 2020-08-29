package linkedlist

import (
	"errors"
	"fmt"
)

type DoublyLinkedList struct {
	head *Node
	tail *Node
	size int
}

// Size() returns current size of doubly linked list
func (dl DoublyLinkedList) Size() int {
	return dl.size
}

// IsEmpty() returns boolean evaluating whether list is empty or not based on its size value
func (dl DoublyLinkedList) IsEmpty() bool {
	return dl.size == 0
}

// Add() adds new Node with integer value to the list
// Either first node in list or at the end of the list
func (dl *DoublyLinkedList) Add(val int) {
	if dl.IsEmpty() {
		dl.AddFirst(val)
	} else {
		dl.AddLast(val)
	}
}

// AddFirst() adds new Node with integer value at the beginnig of list
func (dl *DoublyLinkedList) AddFirst(val int) {
	n := &Node{val: val}
	if dl.IsEmpty() {
		dl.head = n
		dl.tail = n
	} else {
		oldHead := dl.head
		dl.head = n
		dl.head.next = oldHead
		oldHead.prev = dl.head
	}
	dl.size += 1
}

func (dl *DoublyLinkedList) AddLast(val int) {
	prevTail := dl.tail
	dl.tail = &Node{val: val}
	prevTail.next = dl.tail
	dl.tail.prev = prevTail
	dl.size += 1
}

func (dl *DoublyLinkedList) AddAt(idx, val int) (bool, error) {
	if idx > dl.size || idx < 0 {
		return false, &ErrLinkedList{Err: errors.New("Index out of list bounds!")}
	}
	prev := dl.head
	for i, node := 0, dl.head; node != nil; i++ {
		if i == idx {
			newNode := &Node{val, prev, prev.prev}
			prev.next = newNode
			node.prev = newNode
			dl.size += 1
			return true, nil
		}
		prev = node
		node = node.next
	}
	return false, &ErrLinkedList{Err: errors.New("Couldn't add value at specified index!")}
}

func (dl *DoublyLinkedList) RemoveFirst() (int, error) {
	if dl.IsEmpty() {
		return -1, &ErrLinkedList{Err: errors.New("Couldn't remove item!"), Cause: "List is empty!"}
	}
	data := dl.head.Peek()
	newHead := dl.head.next
	dl.head = newHead
	dl.head.prev = nil
	dl.size -= 1
	return data, nil
}

func (dl *DoublyLinkedList) RemoveLast() (int, error) {
	if dl.IsEmpty() {
		return -1, &ErrLinkedList{Err: errors.New("Couldn't remove item!"), Cause: "List is empty!"}
	}
	data := dl.tail.Peek()
	newTail := dl.tail.prev
	dl.tail = newTail
	dl.tail.next = nil
	dl.size -= 1
	return data, nil
}

func (dl DoublyLinkedList) String() string {
	var ret string
	for i, node := 0, dl.head; node != nil; i++ {
		ret = ret + fmt.Sprintf("%d: %d\n", i, node.Peek())
		node = node.next
	}
	return fmt.Sprintf("%s", ret)
}
