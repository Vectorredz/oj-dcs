#include "level_order.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void visit(tree_node *node) {
    printf("visiting node with value %" PRId64 "\n", node->value);
}

tree_node *_tree_node(int64_t value, ll_node *children) {
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    node->value = value;
    node->children = children;
    return node;
}

ll_node *_ll_node(tree_node *child, ll_node *next) {
    ll_node *node = (ll_node*)malloc(sizeof(ll_node));
    node->node = child;
    node->next = next;
    return node;
}

// *********************************************** //


int64_t height(tree_node *root){
    tree_node *curr = root;
    if (curr == NULL){
        return 0;
    }
    int64_t maxHeight = 0;
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


// void levelorder(tree_node *root){
//     tree_node *curr = root;
//     if (curr == NULL){
//         return;
//     }
//     visit(curr);
//     // traverses first; inuubos
//     ll_node *temp = curr->children;
//     while (temp){
//         // if ((temp->node->children)){
//         //     levelorder(temp->node);
//         // }
//         visit(temp->node);
//         temp = temp->next;

//     }


int main() {

    // construct a tree by appending each node to its parent
    int parent[9] = {-1, 0, 0, 0, 1, 1, 1, 3, 6};
    tree_node *nodes[9];
    for (int i = 0; i < 9; i++) {
        nodes[i] = _tree_node(i*10, NULL);
        if (i > 0) {
            int p = parent[i];
            nodes[p]->children = _ll_node(nodes[i], nodes[p]->children);
        }
    }

    tree_node *root = nodes[0];

    // printf("levelorder traversal:\n");
    levelorder(root);

}
