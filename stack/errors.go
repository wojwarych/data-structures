package stack

type ErrorStack struct {
	Err   error
	Cause string
}

func (es *ErrorStack) Error() string {
	return es.Err.Error() + es.Cause
}
