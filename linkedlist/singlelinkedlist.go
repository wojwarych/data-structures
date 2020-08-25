package linkedlist

import (
    "errors"
    "fmt"
)


type SingleLinkedList struct {
    head *Node
    size int
}


func NewSingleLinkedList() SingleLinkedList {
    return SingleLinkedList{nil, 0}
}


func (ll *SingleLinkedList) GetHead() *Node {
    return ll.head
}


func (ll *SingleLinkedList) Size() int {
    return ll.size
}


func (ll *SingleLinkedList) IsEmpty() bool {
    return ll.size == 0
}


func (ll *SingleLinkedList) Add(val int) {
    if ll.IsEmpty() {
        ll.AddFirst(val)
    } else {
        ll.AddLast(val)
    }
}


func (ll *SingleLinkedList) AddFirst(val int) {
    newHead := new(Node)
    newHead.SetVal(val)
    if ll.IsEmpty() {
        ll.head = newHead
    } else {
        prevHead := ll.head
        newHead.next = prevHead
        ll.head = newHead
    }
    ll.size += 1
}


func (ll *SingleLinkedList) AddLast(val int) {
    node := ll.head.next
    prev := ll.head
    for node != nil {
        prev = node
        node = node.next
    }
    n := new(Node)
    n.SetVal(val)
    prev.next = n
    ll.size += 1
}


func (ll *SingleLinkedList) AddAt(idx, val int) (bool, error) {
    if idx > ll.size || idx < 0 {
        return false, errors.New("Index out of list bounds!")
    }
    if idx == 0 {
        ll.AddFirst(val)
        return true, nil
    }
    prev := ll.head
    for i, node := 0, ll.head; node != nil; i++ {
        if idx == i {
            newNode := new(Node)
            newNode.SetVal(val)
            newNode.SetNext(node)
            prev.next = newNode
            ll.size += 1
            return true, nil
        }
        prev = node
        node = node.next
    }
    return false, nil
}


func (ll *SingleLinkedList) Traverse() {
    for node := ll.head; node != nil; {
        fmt.Printf("%d\n", node.Peek())
        node = node.next
    }
}


// func (ll *SingleLinkedList) Get(idx int) (ret int, err error){
//     if idx > ll.size {
//         panic(err)
//     }
//     node := ll.head
//     for i := 0; node != nil; i++ {
//         if i == idx {
//             return node.Peek(), nil
//         }
//         node = node.next
//     }
//     return nil, err
// }


// func (ll *SingleLinkedList) Set(idx, val int) (ret int, err error) {
//     if idx > ll.size {
//         panic(err)
//     }
//     for i, node := 0, ll.head; node != nil; i++ {
//         if i == idx {
//             node.SetVal(val)
//             return node.Peek(), nil
//         }
//         node = node.next
//     }
//     return nil, err
// }


func (ll *SingleLinkedList) IndexOf(val int) int {
    for node, i := ll.head, 0; node != nil; i++{
        if node.Peek() == val {
            return i
        }
    }
    return -1
}


func (ll *SingleLinkedList) PeekFirst() (int, error){
    if ll.IsEmpty() {
        return -1, errors.New("List is empty! No value to show!")
    }
    return ll.head.Peek(), nil
}


func (ll *SingleLinkedList) RemoveLast() (int, error) {
    if ll.IsEmpty() {
        return -1, errors.New("Cannot delete any value! List is empty!")
    }
    node := ll.head
    prev := node
    for node.next != nil {
        prev = node
        node = node.next
    }
    data := node.Peek()
    prev.next = nil
    ll.size -= 1
    return data, nil
}


func (ll *SingleLinkedList) RemoveFirst() (int, error){
    if ll.IsEmpty() {
        return -1, errors.New("Cannot delete any value! List is empty!")
    }
    data := ll.head.Peek()
    ll.head = ll.head.next
    ll.size -= 1
    return data, nil
}


func (ll *SingleLinkedList) Clear() {
    for node := ll.head; node != nil; {
        node = node.next
        ll.head = node
    }
    ll.size = 0
}
