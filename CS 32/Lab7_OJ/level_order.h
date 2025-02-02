#ifndef LEVEL_ORDER_H
#define LEVEL_ORDER_H

#include <stdint.h>

struct tree_node;

typedef struct ll_node {
    struct tree_node *node;
    struct ll_node *next;
} ll_node;

typedef struct tree_node {
    int64_t value;
    struct ll_node *children;
} tree_node;

void visit(tree_node *node);

void levelorder(tree_node *root);

#endif
