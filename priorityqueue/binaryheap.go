package priorityqueue

import (
	"fmt"
	"strings"
)

type BinaryHeap struct {
	heap     []string
	size     int
	capacity int
}

// NewBinaryHeap() returns empty heap for MinPriorityQueue
func NewBinaryHeap() BinaryHeap {
	return BinaryHeap{make([]string, 0, 1), 0, 1}
}

// Add() adds new value to the heap with keeping the constraint on binary heap
func (bh *BinaryHeap) Add(val string) {
	bh.heap = append(bh.heap, val)
	bh.swim(bh.size)
	bh.size += 1
}

func (bh *BinaryHeap) swim(idx int) {
	parent := (idx - 1) / 2
	for idx > 0 && bh.less(idx, parent) {
		bh.swap(parent, idx)
		idx = parent
		parent = (idx - 1) / 2
	}
}

func (bh *BinaryHeap) less(idx, parent int) bool {
	childVal := bh.heap[idx]
	parentVal := bh.heap[parent]
	return strings.Compare(childVal, parentVal) <= 0
}

func (bh *BinaryHeap) swap(parent, idx int) {
	bh.heap[parent], bh.heap[idx] = bh.heap[idx], bh.heap[parent]
}

// Poll() removes value from top of the heap
func (bh *BinaryHeap) Poll() string {
	return bh.removeAt(0)
}

func (bh *BinaryHeap) removeAt(idx int) string {
	lastIdx := bh.size - 1
	bh.swap(lastIdx, idx)
	data := bh.heap[bh.size-1]
	bh.heap = bh.heap[:bh.size-1]
	bh.size -= 1
	bh.sink(idx)
	return data
}

func (bh *BinaryHeap) sink(idx int) {
	for {
		leftChild := 2*idx + 1
		rightChild := 2*idx + 2
		smallest := leftChild
		if rightChild < bh.size && bh.less(rightChild, leftChild) {
			smallest = rightChild
		}
		if leftChild >= bh.size || bh.less(idx, smallest) {
			break
		}
		bh.swap(idx, smallest)
		idx = smallest
	}
}

// Remove() removes searched item from the heap
func (bh *BinaryHeap) Remove(val string) string {
	if idx := bh.Contains(val); idx >= 0 {
		return bh.removeAt(idx)
	}
	return ""
}

// Contains() returns index of value if it exists in the heap
func (bh BinaryHeap) Contains(val string) int {
	for i, v := range bh.heap {
		if v == val {
			return i
		}
	}
	return -1
}

// Peek() shows value of first item in the heap
func (bh BinaryHeap) Peek() string {
	return bh.heap[0]
}

func (bh BinaryHeap) String() string {
	var ret string
	for i, v := range bh.heap {
		ret = ret + fmt.Sprintf("%d: %s ", i, v)
	}
	return ret
}
