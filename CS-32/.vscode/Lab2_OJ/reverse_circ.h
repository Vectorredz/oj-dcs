#ifndef REVERSE_CIRC_H
#define REVERSE_CIRC_H

struct node {
    int val;
    struct node *next;
};

void reverse_circ(struct node *x);

#endif
