#include <stdio.h>
#include <stdlib.h>
#include "bst_slice.h"
#include <stdint.h>

// constuct the BST

bst_node *create_node(int64_t data){
    bst_node *newNode = (bst_node*)malloc(sizeof(bst_node));
    newNode->val = data;
    newNode->left = newNode->right = NULL;

    return newNode;
}

bst_node *build(){
    bst_node *root = create_node(8);
    root->left = create_node(3);
    root->left->left = create_node(1);
    root->left->right = create_node(6);
    root->left->right->right = create_node(7);
    root->left->right->left = create_node(4);

    root->right = create_node(10);
    root->right->right = create_node(14);
    root->right->right->left = create_node(13);

    return root;
}

void inorder_display(bst_node *root){
    if (root == NULL){
        return;
    }
    inorder_display(root->left);
    printf("%ld ", root->val);
    inorder_display(root->right);
}

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



int main(){
    bst_node *root = build();
    int64_t *res = (int64_t*)malloc(100 *sizeof(int64_t));
    int64_t ret = bst_slice(root, 4, 13, res);
    for (int i = 0; i < ret; i++){
        printf("%ld ", res[i]);
    }
    printf("\n");
    inorder_display(root);

}