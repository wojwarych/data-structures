package linkedlist

type ErrLinkedList struct {
	Err   error
	Cause string
}

func (ell *ErrLinkedList) Error() string {
	return ell.Err.Error() + ell.Cause
}
