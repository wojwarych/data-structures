#include <stdlib.h>
#include <sys/types.h>

struct node {
  void *data;
  ssize_t d_size;
  struct node *next;
  struct node *prev;
};

typedef struct node Node;

typedef struct {
  Node *head;
  ssize_t count;
} LList;

typedef struct {
  Node *head;
  Node *tail;
  ssize_t count;
} DLList;

LList *create(void *, ssize_t);
void *destroy(LList *);
void *peek(LList);
Node *find(LList *, void *);
int insert(LList *, void *);
int delete(LList *, void *);

// TODO: probably better to put the interfaces/func definitions as a part of the
// struct
DLList *dl_create(void *, ssize_t);
void *dl_destroy(DLList *);
void *dl_peek(DLList);
Node *dl_find(DLList *, void *);
int dl_insert(DLList *, void *);
int dl_delete(DLList *, void *);
