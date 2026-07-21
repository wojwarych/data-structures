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
  return 0;
}

Node *find(LList *ll, void *data) {
  Node *node = ll->head;
  while (node->next) {
    node = node->next;
    if (*(int *)node->data == *(int *)data) {
      return node;
    }
  }
  return NULL;
}

int delete(LList *ll, void *data) {
  Node *node = ll->head;
  Node *prev = node;
  while (node->next) {
    prev = node;
    node = node->next;
  }
  prev->next = NULL;
  *(int *)data = *(int *)node->data;
  free(node);
  return 0;
}

DLList *dl_create(void *data, ssize_t d_size) {
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
  n->prev = NULL;

  DLList *dllist = malloc(sizeof(DLList));
  if (!dllist) {
    free(d);
    free(n);
    return NULL;
  }
  dllist->head = n;
  dllist->tail = n;
  dllist->count = 1;
  return dllist;
}

void *dl_peek(DLList dll) { return dll.head->data; }

int dl_insert(DLList *dll, void *data) {
  Node *node = dll->head;
  while (node->next) {
    node = node->next;
  }
  Node *new_node = malloc(sizeof(Node));
  if (!new_node) {
    return -1;
  }
  new_node->data = data;
  new_node->next = NULL;
  new_node->prev = node;
  node->next = new_node;
  dll->tail = new_node;
  return 0;
}

void *dl_find(DLList ll, void *data) {
  Node node = *ll.head;
  while (node.next) {
    node = *node.next;
    if (node.data == data) {
      return node.data;
    }
  }
  return NULL;
}

int dl_delete(DLList *dll, void *data) {
  Node *node = dll->tail;
  Node *prev = dll->tail->prev;
  dll->tail = prev;
  *(int *)data = *(int *)node->data;
  free(node);
  return 0;
}
