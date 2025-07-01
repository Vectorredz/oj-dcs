#include "deque.h"
#include <stdlib.h>

bool deque_empty(deque *d)
{
    return (d == NULL || d->leftmost == NULL && d->rightmost == NULL);
}

void deque_push_right(deque *d, int64_t data){
    deque_node *newNode = (deque_node*)oj_malloc(sizeof(deque_node));
    newNode->data = data;
    newNode->left = d->rightmost;
    newNode->right = NULL;
    if (deque_empty(d)){
        d->leftmost = newNode;
    }
    else{
        d->rightmost->right = newNode;
    }
    d->rightmost = newNode;
}

int64_t deque_pop_right(deque *d)
{
    int64_t popped = 0;
    deque_node *temp = NULL;
    popped = d->rightmost->data;
    temp = d->rightmost->left;
    if (d->rightmost->right == NULL && d->rightmost->left == NULL){
        oj_free(d->rightmost);
        d->rightmost = NULL;
        d->leftmost = NULL;
    }
    else {
        d->rightmost->left->right = NULL;
        oj_free(d->rightmost);
        d->rightmost = temp;
    }
    return popped;
}

int64_t deque_pop_left(deque *d){
    int64_t popped = 0;
    deque_node *temp = NULL;
    temp = d->leftmost->right;
    popped = d->leftmost->data;
    if (d->leftmost->right == NULL && d->leftmost->left == NULL){
        oj_free(d->leftmost);
        d->rightmost = NULL;
        d->leftmost = NULL;
    }
    else {
        d->leftmost->right->left = NULL;
        oj_free(d->leftmost);
        d->leftmost = temp;
    }
    return popped;
}

int64_t deque_peek_left(deque *d){
    return (d->leftmost->data);
}

int64_t deque_peek_right(deque *d){
    return (d->rightmost->data);
}

uint32_t deque_size(deque *d)
{
    deque_node *current = d->leftmost;
    uint32_t count = 0;
    while (current){
        count++;
        current = current->right;
    }
    return count;
}