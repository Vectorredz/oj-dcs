#ifndef SPLICE_H
#define SPLICE_H

struct node {
    int val;
    struct node *next;
};

struct node *splice(struct node **ll, int i, int j);

#endif
