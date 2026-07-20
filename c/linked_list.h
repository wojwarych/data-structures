#include <stdlib.h>
#include <sys/types.h>

struct node {
  void *data;
  ssize_t d_size;
  struct node *next;
};

typedef struct node Node;

typedef struct {
  Node *head;
  ssize_t count;
} LList;

LList *create(void *, ssize_t);
void *destroy(LList *);
void *peek(LList);
void *find(LList, void *);
int insert(LList *, void *);
int delete(LList *, void *);
