package linkedlist

import "testing"

var testSet = []int{3, 8, 10, -1, 55}

func TestNewSingleLinkedList(t *testing.T) {
	ll := NewSingleLinkedList()
	if ll.Size() != 0 {
		t.Errorf("Couldn't create empty list! Actual size: %d; Wanted: %d", ll.Size(), 0)
	}
}

func TestAdd(t *testing.T) {
	tables := []struct {
		input     []int
		output    int
		headValue int
	}{
		{[]int{1, 3, 4, 5}, 4, 1},
		{[]int{3}, 1, 3},
		{[]int{2, 4, 8}, 3, 2},
	}
	for _, table := range tables {
		ll := NewSingleLinkedList()
		for _, inp := range table.input {
			ll.Add(inp)
		}
		if size := ll.Size(); size != table.output {
			t.Errorf("SingleLinkedList doesn't size properly! Is: %d; Wanted: %d", size, table.output)
		}
		if head := ll.GetHead().Peek(); head != table.headValue {
			t.Errorf("SingleLinkedList doesn't set head value properly! Is: %d; Wanted: %d", head, table.headValue)
		}
	}
}

func TestIsEmpty(t *testing.T) {
	ll := NewSingleLinkedList()
	if emp := ll.IsEmpty(); emp == false {
		t.Errorf("SingleLinkedList IsEmpty() returns wrong value! Is: %t; Wanted: %t", emp, true)
	}
	ll.Add(2345)
	if emp := ll.IsEmpty(); emp == true {
		t.Errorf("SingleLinkedList IsEmpty() returns wrong value! Is: %t; Wanted: %t", emp, false)
	}
}

func TestAddFirstSetsHead(t *testing.T) {
	ll := NewSingleLinkedList()
	for _, v := range testSet {
		ll.Add(v)
	}
	ll.AddFirst(44)
	if head := ll.GetHead().Peek(); head != 44 {
		t.Errorf("SingleLinkedList AddFirst() returns wrong value! Is: %d; Wanted: %d", head, 44)
	}
}

func TestIndexOf(t *testing.T) {
	ll := NewSingleLinkedList()
	for _, v := range testSet {
		ll.Add(v)
	}
	tables := []struct {
		val int
		ret int
	}{
		{10, 2},
		{-2, -1},
	}
	for _, table := range tables {
		if idx := ll.IndexOf(table.val); idx != table.ret {
			t.Errorf("SingleLinkedList IndexOf() returns wrong value! Is: %d; Wanted: %d", idx, table.ret)
		}
	}
}

func TestAddLastAndRemoveLast(t *testing.T) {
	ll := NewSingleLinkedList()
	for _, v := range testSet {
		ll.Add(v)
	}
	expected := 55
	ret, err := ll.RemoveLast()
	if ret != 55 {
		t.Errorf("SingleLinkedList RemoveLast() returns wrong value! Is: %d; Wants: %d", ret, expected)
	}
	expected = 345
	ll.AddLast(expected)
	if ret, _ := ll.RemoveLast(); ret != expected {
		t.Errorf("SingleLinkedList RemoveLast() returns wrong value! Is: %d; Wants: %d", ret, expected)

	}
	ll = NewSingleLinkedList()
	ret, err = ll.RemoveLast()
	if _, ok := err.(*ErrLinkedList); ret == -1 && !ok {
		t.Errorf("RemoveLast() returned wrong error!")
	}
}

func TestPeekFirst(t *testing.T) {
	ll := NewSingleLinkedList()
	ret, err := ll.PeekFirst()
	if _, ok := err.(*ErrLinkedList); !ok {
		t.Errorf("PeekFirst() returned wrong error on empty list!")
	}
	for _, v := range testSet {
		ll.Add(v)
	}
	if ret, _ = ll.PeekFirst(); ret != 3 {
		t.Errorf("SingleLinkedList PeekFirst returns wrong value! Has: %d; Expects: %d", ret, 3)
	}
}

func TestClear(t *testing.T) {
	ll := NewSingleLinkedList()
	for _, v := range testSet {
		ll.Add(v)
	}
	ll.Clear()
	if ll.IsEmpty() != true && ll.size != 0 {
		t.Errorf("SingleLinkedList Clear() failed to remove all nodes!")
	}
}

func TestAddAt(t *testing.T) {
	ll := NewSingleLinkedList()
	for _, v := range testSet {
		ll.Add(v)
	}
	idx := 2
	val := 1024
	ret, err := ll.AddAt(idx, val)
	if ret != true {
		t.Errorf("SingleLinkedList AddAt() failed to add value %d at desired index: %d", val, idx)
	}
	for _, v := range []int{len(testSet) + 1, -1} {
		ret, err = ll.AddAt(v, val)
		_, ok := err.(*ErrLinkedList)
		if ret != false && !ok {
			t.Errorf("SingleLinkedList AddAt() failed to return proper error value on adding value out of bounds!")
		}
	}
	ll.AddAt(0, val)
	if ll.head.Peek() != val {
		t.Errorf("SingleLinkedList AddAt() failed to add value at the head of list!")
	}
}

func TestRemoveFirst(t *testing.T) {
	ll := NewSingleLinkedList()
	ret, err := ll.RemoveFirst()
	_, ok := err.(*ErrLinkedList)
	if ret != -1 && !ok {
		t.Errorf("SingleLinkedList RemoveFirst() failed to return error on removing item from empty list!")
	}
	for _, v := range testSet {
		ll.Add(v)
	}
	origSize := ll.size
	newHead := testSet[1]
	ret, err = ll.RemoveFirst()
	if ret != newHead && ll.size >= origSize {
		t.Errorf("RemoveFirst() failed to remove first Node of a List!")
	}
}

func TestGet(t *testing.T) {
	ll := NewSingleLinkedList()
	ret, err := ll.Get(2)
	_, ok := err.(*ErrLinkedList)
	if ret != -1 && !ok {
		t.Errorf("Get() failed to return error on retrieving item on empty")
	}
	for _, v := range testSet {
		ll.Add(v)
	}
	ret, _ = ll.Get(1)
	if ret != testSet[1] {
		t.Errorf("Get() failed to get item from list! Has: %d, Wants: %d", ret, testSet[1])
	}
	ret, err = ll.Get(-1)
	_, ok = err.(*ErrLinkedList)
	if ret != -1 && !ok {
		t.Errorf("Get() failed to return error on retrieving item out of bounds of list!")
	}
}

func TestSet(t *testing.T) {
	ll := NewSingleLinkedList()
	val := 1024
	for _, v := range []int{1, -2} {
		ret, err := ll.Set(v, val)
		_, ok := err.(*ErrLinkedList)
		if ret != -1 && !ok {
			t.Errorf("Set() failed to return error on setting item out of bounds of list!")
		}
	}
	for _, v := range testSet {
		ll.Add(v)
	}
	idx := 2
	ret, err := ll.Set(idx, val)
	if ret != testSet[2] && err != nil {
		t.Errorf("Set() failed to modify value on desired index!")
	}
}
