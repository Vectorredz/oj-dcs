#include <stdio.h>
#include <stdlib.h>
#include "bucketize.h"


void Push(struct node **headRef, int key, int val) {
    struct node *temp = malloc(sizeof(struct node));
    temp->key = key;
    temp->val = val;
    temp->next = *headRef;
    *headRef = temp;
}

void Display(struct node *head) {
    struct node *current = head;
    while (current != NULL) {
        printf("(%d, %d) -> ", current->key, current->val);
        current = current->next;
    }
    printf("NULL\n");
}

struct node* BuildList() {
    struct node *head = NULL;
    Push(&head, 5, 50);
    Push(&head, 1, 10);
    Push(&head, 4, 40);
    Push(&head, 1, 15);
    Push(&head, 3, 30);
    return head;
}

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

int main() {
    struct node *head = BuildList();
    Display(head);

    struct node **res;
    int bucketCount = bucketize(head, &res);

    printf("\nBuckets:\n");
    for (int i = 0; i < bucketCount; i++) {
        printf("Bucket %d: ", i);
        Display(res[i]);
    }

    free(res);
    return 0;
}
