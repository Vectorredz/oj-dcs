#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char data;
    struct node *left;
    struct node *right;
    char leftThread;
    char rightThread;
} Node;

typedef struct BinaryTree {
    Node *root;
} BinaryTree;

Node *node_map[256]; // map character label to node pointer

Node *create_node(char data) {
    if (data == '-') return NULL;
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    newNode->leftThread = newNode->rightThread = 0;
    return newNode;
}

Node *get_or_create_node(char data) {
    if (data == '-') return NULL;
    if (!node_map[(int)data])
        node_map[(int)data] = create_node(data);
    return node_map[(int)data];
}

BinaryTree *init_tree() {
    BinaryTree *bTree = (BinaryTree *)malloc(sizeof(BinaryTree));
    bTree->root = NULL;
    return bTree;
}

void build_tree_line(char parent, char left, char right, BinaryTree *b) {
    Node *p = get_or_create_node(parent);
    Node *l = get_or_create_node(left);
    Node *r = get_or_create_node(right);

    p->left = l;
    p->right = r;

    if (!b->root)
        b->root = p;
}

void threadify(Node *root, Node **prev) {
    if (root == NULL) return;

    // Left subtree
    threadify(root->left, prev);

    // Current node
    if (root->left == NULL) {
        root->left = *prev;
        root->leftThread = 1;
    }
    if (*prev && (*prev)->right == NULL) {
        (*prev)->right = root;
        (*prev)->rightThread = 1;
    }

    *prev = root;

    // Right subtree
    threadify(root->right, prev);
}

Node *leftmost_node(Node *root){
    if (!root->left) return root;
    else leftmost_node(root->left);
}

void inorder_threaded(Node *root) {
    Node *curr = root;

    // Go to the leftmost node
    while (curr && curr->left && !curr->leftThread)
        curr = curr->left;

    while (curr) {
        printf("%c ", curr->data);

        // If this node has a threaded right pointer, follow it
        if (curr->rightThread)
            curr = curr->right;
        else {
            // Else go to the leftmost node in right subtree
            curr = curr->right;
            while (curr && curr->left && !curr->leftThread)
                curr = curr->left;
        }
    }
}

void recursive_inorder(Node *root) {
    if (root == NULL) return;
    recursive_inorder(root->left);
    printf("%c ", root->data);
    recursive_inorder(root->right);
}

int main() {
    int n;
    scanf("%d", &n);
    getchar(); // consume newline

    BinaryTree *b = init_tree();

    for (int i = 0; i < n; i++) {
        char parent, left, right;
        scanf("%c %c %c", &parent, &left, &right);
        getchar(); // consume newline after each line
        build_tree_line(parent, left, right, b);
    }
    // printf("%c ", leftmost_node(b->root)->data);
    printf("Recursive In-order Traversal: ");
    recursive_inorder(b->root);
    printf("\n");

    Node *prev = NULL;
    threadify(b->root, &prev);

    printf("Threaded In-order Traversal: ");
    inorder_threaded(b->root);
    printf("\n");

    return 0;
}
