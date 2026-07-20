#include "arr.h"
#include <stdlib.h>
#include <string.h>

Array *create(int capacity) {
  int *container = malloc(sizeof(int) * capacity);
  if (!container) {
    return NULL;
  }
  Array *arr = malloc(sizeof(Array));
  if (!arr) {
    free(container);
    return NULL;
  }
  arr->size = capacity;
  arr->length = 0;
  arr->data = (void *)container;
  arr->d_size = sizeof(int);
  return arr;
}

void destroy(Array *arr) {
  free(arr->data);
  free(arr);
}

int _resize(Array *arr) {
  ssize_t new_cap = arr->size * GROWTH_FACTOR;
  if (new_cap == arr->size) {
    ++new_cap;
  }
  void *tmp = realloc(arr->data, new_cap * arr->d_size);
  if (tmp == NULL) {
    return -1;
  }
  arr->data = tmp;
  arr->size = new_cap;
  return 0;
}

int push(void *value, Array *arr) {
  if ((double)arr->length / arr->size >= 0.75) {
    int ret = _resize(arr);
    if (ret < 0) {
      return -1;
    }
  }
  void *target = (char *)arr->data + arr->length * arr->d_size;
  memcpy(target, value, arr->d_size);
  arr->length++;
  return 0;
}

int pop(void *value, Array *arr) {
  void *target = (char *)arr->data + (arr->length - 1) * arr->d_size;
  memcpy(value, target, arr->d_size);
  arr->length--;
  return 0;
}
