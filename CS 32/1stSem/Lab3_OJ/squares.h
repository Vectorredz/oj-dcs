#ifndef SQUARES_H
#define SQUARES_H

struct node {
    int val;
    struct node *next;
};

int squares(struct node *head, int **res);

#endif
