#include <stdlib.h>
#include "bst_slice.h"
#include <stdint.h>

size_t helper(bst_node *bst, int64_t x, int64_t y, int64_t *res, size_t len){
    if (bst == NULL){
        return len;
    }
    if (bst->val > x){
        len = helper(bst->left, x, y, res, len);
    }
    if (bst->val >= x && bst->val <= y){
        res[len++] = bst->val;
    }
    if (bst->val < y){
        len = helper(bst->right, x, y, res, len);
    }
    return len;
}

size_t bst_slice(bst_node *bst, int64_t x, int64_t y, int64_t *res){
    size_t len = 0;
    return helper(bst, x, y, res, len);
}
