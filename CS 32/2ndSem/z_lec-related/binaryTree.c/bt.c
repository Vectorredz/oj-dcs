#include <stdio.h>
#include <stdlib.h>
#include "header.h"

// INIT

BinaryTree *init_tree(){
    BinaryTree *tree = malloc(sizeof(BinaryTree));
    tree->root = NULL;
    return tree;
}

Node *make_node(char val){
    Node *newNode = malloc(sizeof(Node));
    newNode->val = val;
    newNode->left = newNode->right = NULL;
}

Queue *init_queue(){
    Queue *q = malloc(sizeof(Queue));
    q->front = q->rear = NULL;
}

void enqueue(Queue *q, Node *newNode){
    if (!q->front){
        q->front = q->rear = newNode;
    }
    else {
        q->rear->right = newNode;
        q->rear = newNode;
    }
    return;
    
}

Node *dequeue(Queue *q){
    // if (!q->front) return;
    Node *temp = q->front->right;
    q->front->right = NULL;
    free(q->front);
    q->front = temp;
    return q->front;

}

// TRAVERSALS

void preorder_traversal(Node *root){
    if (root == NULL){ // next node is empty
        // printf("%d", root->val);
        return;
    }
    preorder_traversal(root->left);
    printf("%d", root->val);
    preorder_traversal(root->right);
}


void level_order_traversal(Node *root, Queue *Q){
    // if (root == NULL) return;
    if (Q->front == NULL){
        enqueue(Q, root);
    }
    while (Q->front != NULL){
        Node *curr = dequeue(Q);
        printf("%c -> ", curr->val);
        if (curr->left){
            enqueue(Q, curr->left);
            // level_order_traversal(root->left, Q);
        }
        if (curr->right){
            enqueue(Q, curr->right);
            // level_order_traversal(root->right, Q);
        }
    }
    
    
    
}

int main(){
    BinaryTree *Tree = init_tree();
    Queue *Q = init_queue();

    Tree->root = make_node('F');
    Tree->root->left = make_node('B');
    Tree->root->right = make_node('G');
    Tree->root->left->left = make_node('A');
    Tree->root->left->right = make_node('D');
    // Tree->root->left->right->left = make_node('C');
    // Tree->root->left->right->right = make_node('E');
    Tree->root->right->right = make_node('I');
    Tree->root->right->left = make_node('K');
    // Tree->root->right->right->left = make_node('H');
    // preorder_traversal(Tree->root);
    level_order_traversal(Tree->root, Q);



}