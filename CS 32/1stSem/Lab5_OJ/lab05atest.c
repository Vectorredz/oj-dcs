#include "deque.h"

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define VERIFY(b) do {\
    bool _b = (b);\
    fprintf(stderr, "verifying: %s\n", (#b));\
    if (!_b) {\
        fprintf(stderr, "verification failed!\n");\
        exit(1);\
    }\
} while (0)

deque deque_init() {
    deque d = {NULL, NULL, 0};
    return d;
}

bool deque_empty(deque *d)
{
    return (d->leftmost == NULL && d->rightmost == NULL);
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

void deque_push_left(deque *d, int64_t data) {
    deque_node *newNode = (deque_node*)oj_malloc(sizeof(deque_node));
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

int64_t deque_pop_right(deque *d)
{
    int64_t popped = 0;
    deque_node *temp = NULL;
    if (d->rightmost == d->leftmost){
        popped = d->rightmost->data;
        d->rightmost = NULL;
        d->leftmost = NULL;
    }
    else {
        popped = d->rightmost->data;
        temp = d->rightmost->left;
        d->rightmost->left->right = NULL;
        oj_free(d->rightmost);
        d->rightmost = temp;
    }
    return popped;
}

int64_t deque_pop_left(deque *d){
    int64_t popped = 0;
    deque_node *temp = NULL;
    if (d->rightmost == d->leftmost){
        popped = d->leftmost->data;
        d->rightmost = NULL;
        d->leftmost = NULL;
    }
    else {
        popped = d->leftmost->data;
        temp = d->leftmost->right;
        d->leftmost->right = NULL;
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
    deque_node *current = (deque_node*)oj_malloc(sizeof(deque_node));
    current = d->leftmost;
    uint32_t count = 0;
    while (current){
        count++;
        current = current->right;
    }
    return count;
}

void *oj_malloc(size_t size) {
    assert(size == sizeof(deque_node));
    return malloc(size);
}

void oj_free(void *ptr) {
    free(ptr);
}

void display(deque *d){
    deque_node *temp = d->leftmost;
    while (temp){
        printf("%d -> ", d->leftmost->data);
        temp = temp->right;
    }
    printf("NULL \n");
}


int main() {
    deque q1 = deque_init();
    deque_push_left(&q1, 5);
    deque_pop_left(&q1);
    display(&q1);

    printf("test passed!\n");
}