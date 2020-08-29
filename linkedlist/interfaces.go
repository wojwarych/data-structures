package linkedlist

type LinkedList interface {
	Adder
	Remover
}

type Adder interface {
	Add(int)
	AddFirst(int)
	AddLast(int)
	AddAt(int, int) (bool, error)
}

type Remover interface {
	RemoveFirst() (int, error)
	RemoveLast() (int, error)
}
