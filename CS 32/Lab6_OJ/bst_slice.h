#ifndef BST_SLICE_H
#define BST_SLICE_H

#include <stddef.h>
#include <stdint.h>

typedef struct bst_node {
    int64_t val;
    struct bst_node *left;
    struct bst_node *right;
} bst_node;

size_t bst_slice(bst_node *bst, int64_t x, int64_t y, int64_t *res);

#endif
