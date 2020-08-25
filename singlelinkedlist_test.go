package main

import (
    "testing"

    linkedlist "github.com/warycwoj/data-structures/linkedlist"
)


func TestNewSingleLinkedList(t *testing.T) {
    ll := linkedlist.NewSingleLinkedList()
    if ll.Size() != 0 {
        t.Errorf("Couldn't create empty list! Actual size: %d; Wanted: %d", ll.Size(), 0)
    }
}


func TestSingleLinkedListAddsProperly(t *testing.T) {
    tables := []struct{
        input []int
        output int
        headValue int
    }{
        {[]int{1, 3, 4, 5}, 4, 1},
        {[]int{3}, 1, 3},
        {[]int{2, 4, 8}, 3, 2},
    }
    for _, table := range tables {
        ll := linkedlist.NewSingleLinkedList()
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

