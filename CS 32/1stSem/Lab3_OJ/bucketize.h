#ifndef BUCKETIZE_H
#define BUCKETIZE_H

struct node {
    int key;
    int val;
    struct node *next;
};

int bucketize(struct node *head, struct node ***res);

#endif
