package stack

type Stack interface {
	Pusher
	Popper
}

type Pusher interface {
	Push(int) error
}

type Popper interface {
	Pop() (int, error)
}
