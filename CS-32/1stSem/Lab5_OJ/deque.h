#ifndef DEQUE_H
#define DEQUE_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

void *oj_malloc(size_t size);
void oj_free(void *ptr);

typedef struct deque_node {
    int64_t data;
    struct deque_node *left;
    struct deque_node *right;
} deque_node;

typedef struct deque {
    struct deque_node *leftmost;
    struct deque_node *rightmost;
    uint32_t size;
} deque;

deque deque_init(void);
void deque_push_left(deque *d, int64_t data);
void deque_push_right(deque *d, int64_t data);
int64_t deque_peek_left(deque *d);
int64_t deque_peek_right(deque *d);
int64_t deque_pop_left(deque *d);
int64_t deque_pop_right(deque *d);
bool deque_empty(deque *d);
uint32_t deque_size(deque *d);

#endif
