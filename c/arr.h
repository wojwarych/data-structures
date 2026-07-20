#include <stdlib.h>
#include <sys/types.h>

#define GROWTH_FACTOR 1.5

typedef struct {
  ssize_t size;
  ssize_t length;
  void *data;
  size_t d_size;
} Array;

Array *create(int);
void destroy(Array *);
int push(void *, Array *);
int pop(void *, Array *);
