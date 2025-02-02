#include "level_order.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int64_t height(tree_node *root){
    tree_node *curr = root;
    if (curr == NULL){
        return 0;
    }
    int64_t maxHeight = 1;
    ll_node *temp = curr->children;
    while(temp){
        int64_t childHeight = height(temp->node);
        if (childHeight > maxHeight){
            maxHeight = childHeight;
        }
        temp = temp->next;
    }
    return 1 + maxHeight;
}

void printLevel(tree_node *root, int64_t level){
    if (root == NULL){
        return;
    }
    if (level == 1){
        visit(root);
    }
    else {
        ll_node *temp = root->children;
        while (temp){
            printLevel(temp->node, level-1);
            temp = temp->next;
        }
    }
}

void display(tree_node *root){
    int64_t h = height(root);
    for (int64_t i = 1; i <= h; i++){
        printLevel(root, i);
    }
}

void levelorder(tree_node *root){
    return display(root);
}
