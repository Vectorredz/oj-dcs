#include "rdeque.h"
#include <stdlib.h>

typedef struct deque_node {
    int64_t data;
    struct deque_node *left;
    struct deque_node *right;
} deque_node;

typedef struct deque {
    struct deque_node *leftmost;
    struct deque_node *rightmost;
    int reversed;
    uint32_t size;
} deque;

deque *deque_init(void){
    deque *d = (deque*)malloc(sizeof(deque));
    d->leftmost = NULL;
    d->rightmost = NULL;
    d->size = 0;
    d->reversed = 0;
    return d;
}

bool deque_empty(deque *d)
{
    return (d == NULL || d->leftmost == NULL && d->rightmost == NULL);
}

void deque_push_right(deque *d, int64_t data){
    deque_node *newNode = (deque_node*)malloc(sizeof(deque_node));
    if (d->reversed){
        newNode->data = data;
        newNode->left = NULL;
        newNode->right = d->leftmost;
        if (deque_empty(d)){
            d->rightmost = newNode;
        }
        else{
            d->leftmost->left = newNode;
        }
        d->leftmost = newNode;
    }
    else {
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
}

void deque_push_left(deque *d, int64_t data) {
    deque_node *newNode = (deque_node*)malloc(sizeof(deque_node));
    if (d->reversed){
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
    else {
        newNode->data = data;
        newNode->left = NULL;
        newNode->right = d->leftmost;
        if (deque_empty(d)){
            d->rightmost = newNode;
        }
        else{
            d->leftmost->left = newNode;
        }
        d->leftmost = newNode;
    }
}

int64_t deque_pop_right(deque *d)
{
    int64_t popped = 0;
    deque_node *temp = NULL;
    if (d->reversed){
        temp = d->leftmost->right;
        popped = d->leftmost->data;
        if (d->leftmost->right == NULL && d->leftmost->left == NULL){
            free(d->leftmost);
            d->rightmost = NULL;
            d->leftmost = NULL;
        }
        else {
            d->leftmost->right->left = NULL;
            free(d->leftmost);
            d->leftmost = temp;
        }
    }
    else {
        popped = d->rightmost->data;
        temp = d->rightmost->left;
        if (d->rightmost->right == NULL && d->rightmost->left == NULL){
            free(d->rightmost);
            d->rightmost = NULL;
            d->leftmost = NULL;
        }
        else {
            d->rightmost->left->right = NULL;
            free(d->rightmost);
            d->rightmost = temp;
        }
    }
    return popped;
}

int64_t deque_pop_left(deque *d){
    int64_t popped = 0;
    deque_node *temp = NULL;
    if (d->reversed){
        popped = d->rightmost->data;
        temp = d->rightmost->left;
        if (d->rightmost->right == NULL && d->rightmost->left == NULL){
            free(d->rightmost);
            d->rightmost = NULL;
            d->leftmost = NULL;
        }
        else {
            d->rightmost->left->right = NULL;
            free(d->rightmost);
            d->rightmost = temp;
        }
    }
    else {
        temp = d->leftmost->right;
        popped = d->leftmost->data;
        if (d->leftmost->right == NULL && d->leftmost->left == NULL){
            free(d->leftmost);
            d->rightmost = NULL;
            d->leftmost = NULL;
        }
        else {
            d->leftmost->right->left = NULL;
            free(d->leftmost);
            d->leftmost = temp;
        }
    }
    return popped;
}

int64_t deque_peek_left(deque *d){
    if (d->reversed){
        return (d->rightmost->data);
    }
    else {
        return (d->leftmost->data);
    }
}

int64_t deque_peek_right(deque *d){
    if (d->reversed){
        return (d->leftmost->data);
    }
    else {
        return (d->rightmost->data);
    }
}

uint32_t deque_size(deque *d)
{
    deque_node *current = (deque_node*)malloc(sizeof(deque_node));
    current = d->leftmost;
    uint32_t count = 0;
    while (current){
        count++;
        current = current->right;
    }
    return count;
}

void deque_reverse(deque *d)
{
    if (d->reversed == 0){
        d->reversed = 1;
    }
    else {
        d->reversed = 0;
    }
}