#include "pre_post_order.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// ************************************************************ //

void preorder(tree_node *root){
    tree_node *curr = root;
    if (root == NULL){
        return;
    }
    visit(root);
    ll_node *temp = curr->children;
    while (temp){
        preorder(temp->node);
        temp = temp->next;
    }
}
void postorder(tree_node *root){
      tree_node *curr = root;
    if (root == NULL){
        return;
    }
    ll_node *temp = curr->children;
    while (temp){
        postorder(temp->node);
        temp = temp->next;
    }
    visit(root);
}