package linkedlist

// Node is struct implementing basic structure of Node in linked list
type Node struct {
	val  int
	next *Node
	prev *Node
}

// Peek() returns value stored in Node
func (n Node) Peek() int {
	return n.val
}

// SetVal() sets new value stored in Node
func (n *Node) SetVal(val int) {
	n.val = val
}

// GetNext() returns pointer to next Node to which node points to
func (n *Node) GetNext() *Node {
	return n.next
}

// SetNext() sets new next Node to which node points to
func (n *Node) SetNext(otherNode *Node) {
	n.next = otherNode
}

// GetPrev() returns pointer to previous Node to which node points to
func (n *Node) GetPrev() *Node {
	return n.prev
}

// SetPrev() sets new previous Node to which node poomts to
func (n *Node) SetPrev(otherNode *Node) {
	n.prev = otherNode
}
