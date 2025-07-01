#include <stdlib.h>
#include "bucketize.h"

int bucketize(struct node *head, struct node ***res) {
    int maxKey = 0;
    struct node *curr = head;
    while (curr) {
        if (curr->key > maxKey) {
            maxKey = curr->key;
        }
        curr = curr->next;
    }

    int bucketSize = maxKey + 1;
    *res = (struct node **)malloc(bucketSize * sizeof(struct node *));
    
    for (int i = 0; i < bucketSize; i++) {
        (*res)[i] = NULL;
    }

    curr = head;
    while (curr != NULL) {
        int key = curr->key;
        struct node *nextNode = curr->next;
        curr->next = (*res)[key];
        (*res)[key] = curr;
        curr = nextNode;
    }

    return bucketSize;
}