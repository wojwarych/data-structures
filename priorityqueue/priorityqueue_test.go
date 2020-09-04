package priorityqueue

import (
	// "fmt"
	"reflect"
	"testing"
)

func TestNewPQ(t *testing.T) {
	pq := NewBinaryHeap()
	if pq.size != 0 {
		t.Errorf("Wrong init value of size in Priority Queue! Has: %d; Wants: %d", pq.size, 0)
	}
	if pq.capacity != 1 {
		t.Errorf("Wrong init value of capacity in Priority Queue! Has: %d; Wants: %d", pq.capacity, 1)
	}
	if sliceType := reflect.TypeOf(pq.heap).Elem().Kind(); sliceType != reflect.String {
		t.Errorf("Wrong init type of heap in Priority Queue! Has: %T; Wants: %T", sliceType, reflect.String)
	}
}

func TestAddPQ(t *testing.T) {
	pq := NewBinaryHeap()
	for _, v := range []string{"b", "c", "g", "a", "h", "r"} {
		pq.Add(v)
	}
	expectedOrder := []string{"a", "b", "g", "c", "h", "r"}
	size := 6
	if pqSize := pq.size; pq.size != size {
		t.Errorf("Wrong size of heap after adding values! Has: %d; Wants: %d", pqSize, size)
	}
	for i, v := range pq.heap {
		if v != expectedOrder[i] {
			t.Errorf("Values added to heap doesn't comply to Binary Heap invariant! Is: %v; Wants: %v", pq.heap, expectedOrder)
		}
	}
}

func TestPollPQ(t *testing.T) {
	pq := NewBinaryHeap()
	for _, v := range []string{"b", "c", "g", "a", "h", "r"} {
		pq.Add(v)
	}
	expectedItem := []string{"a", "b", "c", "h", "g", "r"}
	for i := 0; i < pq.size; i++ {
		val := pq.Poll()
		if val != expectedItem[i] {
			t.Errorf("Value polled from heap doesn't comply to Binary Heap invariant! Is: %s; Wants: %s", val, expectedItem[i])
		}
	}
}

func TestRemovePQ(t *testing.T) {
	pq := NewBinaryHeap()
	for _, v := range []string{"b", "c", "g", "a", "h", "r"} {
		pq.Add(v)
	}
	pq.Remove("h")
	expectedOrder := []string{"a", "b", "g", "c", "r"}
	for i, v := range expectedOrder {
		if pq.heap[i] != v {
			t.Errorf("Value removed from heap crashes Binary Heap invariant! Heap structure is: %v; Wants: %v", pq.heap, expectedOrder)
		}
	}
}

func TestPeekPQ(t *testing.T) {
	pq := NewBinaryHeap()
	for _, v := range []string{"b", "c", "g", "a", "h", "r", "f"} {
		pq.Add(v)
	}
	expectedItem := "a"
	if val := pq.Peek(); val != expectedItem {
		t.Errorf("Value peeked from heap is invalid! Is: %s; Wants: %s", val, expectedItem)
	}
}

func TestContainsPQ(t *testing.T) {
	pq := NewBinaryHeap()
	for _, v := range []string{"b", "c", "g", "a", "h", "r", "f"} {
		pq.Add(v)
	}
	idx := pq.Contains("xx")
	if idx != -1 {
		t.Errorf("Contains() didn't returned -1 for non existent item in heap!")
	}
}

func TestRemoveEmptyStringPQ(t *testing.T) {
	pq := NewBinaryHeap()
	for _, v := range []string{"b", "c", "g", "a", "h", "r", "f"} {
		pq.Add(v)
	}
	val := pq.Remove("xx")
	if val != "" {
		t.Errorf("Remove() didn't returned empty string for non existent item in heap!")
	}
}
