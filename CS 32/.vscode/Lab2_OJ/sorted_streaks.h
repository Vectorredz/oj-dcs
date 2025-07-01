#ifndef SORTED_STREAKS_H
#define SORTED_STREAKS_H

struct node {
    int val;
    struct node *next;
};

int sorted_streaks(struct node *head, struct node **result);

#endif
