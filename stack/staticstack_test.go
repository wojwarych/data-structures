package stack

import (
	"testing"
)

const testSize = 5

func TestNewStaticStack(t *testing.T) {
	ss := NewStaticStack(testSize)
	if !ss.IsEmpty() || ss.size != 0 || ss.maxSize != testSize {
		t.Errorf("Static stack did not initialize correctly!")
	}
}

func TestStaticStackPush(t *testing.T) {
	ss := NewStaticStack(testSize)
	val := 10
	ss.Push(val)
	if val, _ := ss.Peek(); val != 10 {
		t.Errorf("Static stack did not pushed new item correctly! Has: %v; Wants: %d", ss.top, val)
	}
}

func TestStaticStackPushOverflow(t *testing.T) {
	ss := NewStaticStack(testSize)
	for _, v := range []int{1, 2, 3, 4, 5} {
		ss.Push(v)
	}
	overFlowVal := 6
	err := ss.Push(overFlowVal)
	_, ok := err.(*ErrorStack)
	if err == nil {
		t.Errorf("Static stack didn't overflow on pushing over the max size!")
	}
	if !ok {
		t.Errorf("Error returned with push overflow is of incorrect type!")
	}
}

func TestStaticStackPeekFail(t *testing.T) {
	ss := NewStaticStack(testSize)
	val, err := ss.Peek()
	if val != -1 && err == nil {
		t.Errorf("Peek() did not return error at peeking empty static stack!")
	}
	_, ok := err.(*ErrorStack)
	if !ok {
		t.Errorf("Peek() on empty stack returned error of wrong type!")
	}
}

func TestStaticStackPass(t *testing.T) {
	ss := NewStaticStack(testSize)
	ss.Push(10)
	ss.Push(20)
	val, err := ss.Peek()
	if val != 20 && err != nil {
		t.Errorf("Peek() returned error on correct pushing of stack!")
	}
}

func TestStaticStackSize(t *testing.T) {
	ss := NewStaticStack(testSize)
	testValues := []int{1, 2, 3, 4, 5}
	for _, v := range testValues {
		ss.Push(v)
	}
	if ss.Size() != len(testValues) {
		t.Errorf("Size() returns wrong size of Stack! Has: %d; Wants: %d", ss.Size(), len(testValues))
	}
}

func TestStaticStackPopEmptyStack(t *testing.T) {
	ss := NewStaticStack(testSize)
	ret, err := ss.Pop()
	if ret != -1 && err == nil {
		t.Errorf("Pop() did not returned error on removing item from empty stack!")
	}
}

func TestStaticStackPopPopulatedStack(t *testing.T) {
	ss := NewStaticStack(testSize)
	testItems := []int{1, 2, 3, 4, 5}
	for _, v := range testItems {
		ss.Push(v)
	}
	ret, err := ss.Pop()
	lastItem := testItems[len(testItems)-1]
	if ret != lastItem && err != nil {
		t.Errorf("Pop() did not returned correct value on removing item from populated stack!; Has: %d; Wants: %d", ret, lastItem)
	}
}
