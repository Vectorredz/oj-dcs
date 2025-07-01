#ifndef EVEN_H
#define EVEN_H

struct node {
    int val;
    struct node *next;
};

struct node *even(struct node *head);

#endif
