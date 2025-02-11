#include <stdlib.h>
#include "bqueue.h"

typedef struct queue_node {
    int64_t data;
    struct queue_node *left;
    struct queue_node *right;
} queue_node;

typedef struct queue {
    struct queue_node *leftmost;
    struct queue_node *rightmost;
    struct queue_node *minleft;
    struct queue_node *minright;
    int64_t size;
    struct queue *q2;
} queue;

queue *queue_init(void) {
    queue *d = (queue *)malloc(sizeof(queue));
    d->leftmost = NULL;
    d->rightmost = NULL;
    d->minleft = NULL;
    d->minright = NULL;
    d->size = 0;
    d->q2 = (queue *)malloc(sizeof(queue));
    d->q2->leftmost = NULL;
    d->q2->rightmost = NULL;
    d->q2->minleft = NULL;
    d->q2->minright = NULL;
    d->q2->size = 0;
    return d;
}

int is_queue_empty(queue *d) {
    return (d->leftmost == NULL);
}

int is_monotonic_queue_empty(queue *d) {
    return (d->q2->leftmost == NULL);
}

void enqueue(queue *d, int64_t val) {
    queue_node *newnode = (queue_node *)malloc(sizeof(queue_node));
    newnode->data = val;
    newnode->left = NULL;
    newnode->right = NULL;

    if (d->rightmost == NULL) {
        d->leftmost = d->rightmost = newnode;
    } else {
        d->rightmost->right = newnode;
        newnode->left = d->rightmost;
        d->rightmost = newnode;
    }

    queue_node *temp = (queue_node *)malloc(sizeof(queue_node));
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;

    if (d->q2->rightmost == NULL || val < d->q2->leftmost->data) {
        temp->right = d->q2->leftmost;
        if (d->q2->leftmost != NULL) {
            d->q2->leftmost->left = temp;
        }
        d->q2->leftmost = temp;
        if (d->q2->rightmost == NULL) {
            d->q2->rightmost = temp;
        }
    } else if (val == d->q2->leftmost->data) {
        if (d->q2->rightmost == NULL) {
            d->q2->leftmost = d->q2->rightmost = temp;
        } else {
            d->q2->rightmost->right = temp;
            temp->left = d->q2->rightmost;
            d->q2->rightmost = temp;
        }
    } else {
        queue_node *current = d->q2->rightmost;
        while (current != NULL && val <= current->data) {
            current = current->left;
        }
        if (current == NULL) {
            temp->right = d->q2->leftmost;
            d->q2->leftmost->left = temp;
            d->q2->leftmost = temp;
        } else {
            temp->right = current->right;
            if (current->right != NULL) {
                current->right->left = temp;
            }
            current->right = temp;
            temp->left = current;
            if (d->q2->rightmost == current) {
                d->q2->rightmost = temp;
            }
        }
    }
}

int64_t dequeue(queue *d) {
    if (is_queue_empty(d)) {
        return 0;
    }

    int64_t val = d->leftmost->data;
    queue_node *temp = d->leftmost;

    if (d->leftmost->right == NULL) {
        d->leftmost = NULL;
        d->rightmost = NULL;
        if (d->q2->leftmost->data == val) {
            queue_node *min_temp = d->q2->leftmost;
            d->q2->leftmost = d->q2->leftmost->right;
            if (d->q2->leftmost != NULL) {
                d->q2->leftmost->left = NULL;
            }
            free(min_temp);
        }
        d->q2->rightmost = NULL;
    } else {
        d->leftmost = d->leftmost->right;
        d->leftmost->left = NULL;

        if (val == d->q2->leftmost->data) {
            queue_node *min_temp = d->q2->leftmost;
            d->q2->leftmost = d->q2->leftmost->right;
            if (d->q2->leftmost != NULL) {
                d->q2->leftmost->left = NULL;
            }
            free(min_temp);
        }
    }

    free(temp);
    return val;
}

int64_t peek_front(queue *d) {
    if (is_queue_empty(d)) {
        return 0;
    }
    return d->leftmost->data;
}

int64_t queue_min(queue *d) {
    if (is_monotonic_queue_empty(d)) {
        return 0;
    }
    return d->q2->leftmost->data;
}