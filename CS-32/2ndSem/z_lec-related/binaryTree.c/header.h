#ifndef BINARY_TREE
#define BINARY_TREE

typedef struct node{
    struct node *left;
    struct node *right;
    char val;
} Node;

typedef struct BinaryTree{
    Node *root;
} BinaryTree;


typedef struct Queue{
    Node *front;
    Node *rear;
} Queue;

#endif