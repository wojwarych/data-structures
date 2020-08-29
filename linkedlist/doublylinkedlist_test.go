package linkedlist

import "testing"

var testDoublySet = []int{3, 66, 88, 99}

func TestDoublyListSize(t *testing.T) {
	dl := &DoublyLinkedList{}
	if size := dl.Size(); size != 0 {
		t.Errorf("Newly created empty DoublyLinkedList doesn't have 0 size! Has: %d", size)
	}
	dl.Add(5)
	expected := 1
	if size := dl.Size(); size != expected {
		t.Errorf("DoublyLinkedList doesn't have proper number as a size! Has: %d; Expects: %d", size, expected)
	}
}

func TestDoublyListAdd(t *testing.T) {
	dl := &DoublyLinkedList{}
	for _, v := range testDoublySet {
		dl.Add(v)
	}
	headVal := testDoublySet[0]
	if head := dl.head.Peek(); head != testDoublySet[0] {
		t.Errorf("Add() doesn't add head Node properly! Has: %d; Expects: %d", head, headVal)
	}
	tailVal := testDoublySet[len(testDoublySet)-1]
	if tail := dl.tail.Peek(); tail != tailVal {
		t.Errorf("Add() doesn't add tail Node properly! Has: %d; Expects: %d", tail, tailVal)
	}
	newHeadVal := 9
	prevHead := dl.head
	dl.AddFirst(9)
	if head, headNext := dl.head.Peek(), dl.head.next; head != newHeadVal && headNext != prevHead {
		t.Errorf("AddFirst() doesn't add new head Node properly! Has: %d, Wants: %d", head, newHeadVal)
	}
	newTailVal := 185
	prevTail := dl.tail
	dl.AddLast(newTailVal)
	if tail, tailPrev := dl.tail.Peek(), dl.tail.prev; tail != newTailVal && tailPrev != prevTail {
		t.Errorf("AddLast() doesn't add new tail Node properly! Has: %d, Wants: %d", tail, newTailVal)
	}
}

func TestDoublyListRemove(t *testing.T) {
	dl := &DoublyLinkedList{}
	ret, err := dl.RemoveFirst()
	_, ok := err.(*ErrLinkedList)
	if ret != -1 && !ok {
		t.Errorf("RemoveFirst() does not return error on removing item on empty list!")
	}
	ret, err = dl.RemoveLast()
	_, ok = err.(*ErrLinkedList)
	if ret != -1 && !ok {
		t.Errorf("RemoveLast() does not return error on removing item on empty list!")
	}
	for _, v := range testDoublySet {
		dl.Add(v)
	}
	ret, _ = dl.RemoveFirst()
	newHead := testDoublySet[1]
	if ret != testDoublySet[0] && dl.head.Peek() != newHead && dl.size != len(testDoublySet)-1 {
		t.Errorf("RemoveFirst() does not remove properly head Node! Is: %d; Expects: %d", ret, newHead)
	}
	ret, _ = dl.RemoveLast()
	newTail := testDoublySet[len(testDoublySet)-2]
	if ret != testDoublySet[len(testDoublySet)-1] && dl.tail.Peek() != newTail && dl.size != len(testDoublySet)-2 {
		t.Errorf("RemoveLast() does not remove properly head Node! Is: %d; Expects: %d", ret, newTail)
	}
}

func TestDoublyListAddAt(t *testing.T) {
	dl := &DoublyLinkedList{}
	ret, err := dl.AddAt(1, 333)
	_, ok := err.(*ErrLinkedList)
	if ret != false && !ok {
		t.Errorf("AddAt() does not return error on adding item on empty list!")
	}
	for _, v := range testDoublySet {
		dl.Add(v)
	}
	ret, err = dl.AddAt(-2, 333)
	_, ok = err.(*ErrLinkedList)
	if ret != false && !ok {
		t.Errorf("AddAt() does not return error on adding item on index out of bounds!")
	}
	idx := 2
	val := 1024
	ret, _ = dl.AddAt(idx, val)
	if ret != true {
		t.Errorf("AddAt() failed to add value %d at desired index: %d", val, idx)
	}
}
