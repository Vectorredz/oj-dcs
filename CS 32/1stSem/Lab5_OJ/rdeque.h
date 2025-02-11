#ifndef RDEQUE_H
#define RDEQUE_H

#include <stdint.h>
#include <stdbool.h>

typedef struct deque deque;

deque *deque_init(void);
void deque_push_left(deque *d, int64_t val);
void deque_push_right(deque *d, int64_t val);
int64_t deque_peek_left(deque *d);
int64_t deque_peek_right(deque *d);
int64_t deque_pop_left(deque *d);
int64_t deque_pop_right(deque *d);
bool deque_empty(deque *d);
uint32_t deque_size(deque *d);
void deque_reverse(deque *d);

#endif
