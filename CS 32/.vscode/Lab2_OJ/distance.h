#ifndef DISTANCE_H
#define DISTANCE_H

struct node {
    int val;
    struct node *next;
};

int distance(struct node *a, struct node *b);

#endif
