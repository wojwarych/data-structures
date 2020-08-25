package linkedlist

type Node struct {
    val int
    next *Node
    prev *Node
}


func (n Node) Peek() int{
    return n.val
}


func (n *Node) SetVal(val int) {
    n.val = val
}


func (n *Node) GetNext() *Node {
    return n.next
}


func (n *Node) SetNext(otherNode *Node) {
    n.next = otherNode
}


func (n *Node) GetPrev() *Node {
    return n.prev
}


func (n *Node) SetPrev(otherNode *Node) {
    n.prev = otherNode
}
