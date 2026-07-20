#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>

LList *create(void *data, ssize_t d_size) {
  void *d = malloc(sizeof(d_size));
  if (!d) {
    return NULL;
  }
  Node *n = malloc(sizeof(Node));
  if (!n) {
    free(d);
    return NULL;
  }
  n->d_size = d_size;
  n->data = data;
  n->next = NULL;

  LList *llist = malloc(sizeof(LList));
  if (!llist) {
    free(d);
    free(n);
    return NULL;
  }
  llist->head = n;
  llist->count = 1;
  return llist;
}

void *peek(LList ll) { return ll.head->data; }

int insert(LList *ll, void *data) {
  Node *node = ll->head;
  while (node->next) {
    node = node->next;
  }
  Node *new_node = malloc(sizeof(Node));
  if (!new_node) {
    return -1;
  }
  new_node->data = data;
  new_node->next = NULL;
  node->next = new_node;
  ll->head = node;
  return 0;
}

void *find(LList ll, void *data) {
  Node node = *ll.head;
  while (node.next) {
    node = *node.next;
    if (node.data == data) {
      return node.data;
    }
  }
  return NULL;
}
