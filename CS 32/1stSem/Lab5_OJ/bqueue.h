#ifndef BQUEUE_H
#define BQUEUE_H

#include <stdint.h>

typedef struct queue queue;

queue *queue_init(void);
void enqueue(queue *d, int64_t val);
int64_t dequeue(queue *d);
int64_t peek_front(queue *d);
int64_t queue_min(queue *d);

#endif
