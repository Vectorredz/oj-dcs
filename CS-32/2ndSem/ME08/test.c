#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define newline printf("\n")

typedef int BinaryTreeDataType;
typedef struct binarytreenode BinaryTreeNode;
struct binarytreenode
{
    int LTAG;             // 1 if LSON is child, 0 if LSON is inorder predecessor thread
    BinaryTreeNode *LSON;
    BinaryTreeDataType DATA;
    BinaryTreeNode *RSON;
    int RTAG;             // 1 if RSON is child, 0 if RSON is inorder successor thread
};


struct edge
{
	int name;
    int lson;
    int rson;
};
typedef struct edge Edge;

// --- Function Prototypes ---
void CREATE(BinaryTreeNode **);
void POSTORDER_T (BinaryTreeNode *); // Will be replaced with iterative version
void PREORDER_T (BinaryTreeNode *);
void INORDER_T (BinaryTreeNode *);
BinaryTreeNode *INSUC(BinaryTreeNode *);
BinaryTreeNode *INPRED(BinaryTreeNode *);
BinaryTreeNode *PRESUC(BinaryTreeNode *);
// BinaryTreeNode *POSTSUC(BinaryTreeNode *); // Flawed function - will be removed
void VISIT (BinaryTreeNode *);
void FREE_TREE (BinaryTreeNode *);
int read_tree_input(Edge **, int **);
int LOOK (int *, int, int);
BinaryTreeNode *create_node(BinaryTreeDataType);


int read_tree_input (Edge **edges, int **inorder_list)
{
	int i, n;
    int lson, rson, name;

	// Read number of nodes
	if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "Error reading number of nodes or invalid number.\n");
        exit(EXIT_FAILURE);
    }
    getchar(); // Consume the newline after the number

    *edges = (Edge *) malloc (n*sizeof(Edge));
    if (*edges == NULL) {
        perror("Failed to allocate memory for edges");
        exit(EXIT_FAILURE);
    }

    // Read edge information
    for (i = 0; i < n; i++)
    {
        (*edges)[i].name = i+1;

        if (scanf("%d %d", &lson, &rson) != 2) {
             fprintf(stderr, "Error reading edge data for node %d.\n", i+1);
             free(*edges);
             exit(EXIT_FAILURE);
        }
        getchar(); // Consume the newline
        (*edges)[i].lson = lson;
        (*edges)[i].rson = rson;
    }

    *inorder_list = (int *) malloc (n*sizeof(int));
     if (*inorder_list == NULL) {
        perror("Failed to allocate memory for inorder_list");
        free(*edges);
        exit(EXIT_FAILURE);
    }

    // Read inorder traversal sequence
    for (i = 0; i < n; i++)
    {
        // Expecting format like -X-
        if (scanf("-%d-", &name) != 1) {
             fprintf(stderr, "Error reading inorder list data at index %d.\n", i);
             free(*edges);
             free(*inorder_list);
             exit(EXIT_FAILURE);
        }
        (*inorder_list)[i] = name;
    }
    // No need for extra getchar() here if format is strictly -X-

	return n;
}

void CREATE (BinaryTreeNode **H)
{
	Edge *edges;
    int *inorder_list;
    BinaryTreeNode **nodes; // Array to hold pointers to the created nodes
    BinaryTreeNode *head;
	int n;
	int i = 0, index;

	n = read_tree_input(&edges, &inorder_list);

    /**
    Head node of the threaded binary tree.
    DATA = -1 (or some sentinel value)
    LSON points to root, LTAG = 1 (indicates child pointer)
    RSON points to itself, RTAG = 1 (indicates child pointer, convention)
    **/
    head = (BinaryTreeNode *) malloc (sizeof(BinaryTreeNode));
     if (head == NULL) {
        perror("Failed to allocate memory for head node");
        exit(EXIT_FAILURE); // Or handle error appropriately
    }
    head->DATA = -1; // Sentinel value
    head->RSON = head; // Points to itself
    head->RTAG = 1;    // Conventionally treated as a link for traversal termination
    head->LSON = head; // Initially points to self (empty tree)
    head->LTAG = 0;    // Indicates no actual left child (points to root eventually)

    if (n == 0) { // Handle empty tree case
        *H = head;
        free(edges);
        free(inorder_list);
        return;
    }

    nodes = (BinaryTreeNode **) malloc (n*sizeof(BinaryTreeNode*));
     if (nodes == NULL) {
        perror("Failed to allocate memory for nodes array");
        free(head);
        free(edges);
        free(inorder_list);
        exit(EXIT_FAILURE);
    }

	// Create all nodes first
	for (i = 0; i < n; i++)
    {
        nodes[i] = (BinaryTreeNode *) malloc (sizeof(BinaryTreeNode));
         if (nodes[i] == NULL) {
            perror("Failed to allocate memory for a tree node");
            // Free previously allocated nodes, head, etc.
             exit(EXIT_FAILURE);
        }
        nodes[i]->DATA = edges[i].name;
        nodes[i]->LSON = NULL; // Initialize pointers
        nodes[i]->LTAG = 0;    // Initialize tags (assume thread initially)
        nodes[i]->RSON = NULL;
        nodes[i]->RTAG = 0;
    }

    head->LSON = nodes[0]; // Head's left points to the root (node 1, index 0)
    head->LTAG = 1;        // This is a child link

    /*
    Creates the regular child links and inorder thread links
    */
    for (i = 0; i < n; i++)
    {
        // --- Set Left Link ---
        if (edges[i].lson > 0) // If a left child exists
        {
            nodes[i]->LSON = nodes[edges[i].lson-1]; // Point to child node
            nodes[i]->LTAG = 1;                     // Mark as child link
        }
        else // No left child, create inorder predecessor thread
        {
            index = LOOK (inorder_list, n, edges[i].name);
            if (index == -1) { /* Handle error: node not found in inorder list */ }

            if (index == 0) // Node is the first in inorder traversal
                nodes[i]->LSON = head; // Thread points to head
            else
                // Thread points to inorder predecessor
                nodes[i]->LSON = nodes[inorder_list[index-1]-1];

            nodes[i]->LTAG = 0; // Mark as thread link
        }

        // --- Set Right Link ---
        if (edges[i].rson > 0) // If a right child exists
        {
            nodes[i]->RSON = nodes[edges[i].rson-1]; // Point to child node
            nodes[i]->RTAG = 1;                     // Mark as child link
        }
        else // No right child, create inorder successor thread
        {
            index = LOOK (inorder_list, n, edges[i].name);
             if (index == -1) { /* Handle error: node not found in inorder list */ }

            if (index == n-1) // Node is the last in inorder traversal
                nodes[i]->RSON = head; // Thread points to head
            else
                // Thread points to inorder successor
                nodes[i]->RSON = nodes[inorder_list[index+1]-1];

            nodes[i]->RTAG = 0; // Mark as thread link
        }
    }

    *H = head;

	// Free temporary structures
	free(edges);
    free(inorder_list);
    free(nodes); // Free the array of pointers, not the nodes themselves yet
}

void VISIT(BinaryTreeNode *T)
{
    if (T && T->DATA != -1) { // Don't visit the head node's data
        printf("-%d-", T->DATA);
    }
}

/**
 Recursive Free Tree (Postorder traversal logic)
 NOTE: Be cautious with deep trees causing stack overflow.
 An iterative approach using the corrected POSTORDER_T logic
 would be safer for very large trees.
 **/
void FREE_TREE_RECURSIVE(BinaryTreeNode *node) {
    if (node == NULL || node->DATA == -1) { // Stop at head or NULL
        return;
    }
    // Only recurse down actual child links, not threads
    if (node->LTAG == 1) {
        FREE_TREE_RECURSIVE(node->LSON);
    }
    if (node->RTAG == 1) {
        FREE_TREE_RECURSIVE(node->RSON);
    }
    // Free the node itself after its children (postorder)
    // printf("Freeing node: %d\n", node->DATA); // Debug print
    free(node);
}

// Wrapper function to start freeing from the root
void FREE_TREE(BinaryTreeNode *H) {
    if (H == NULL) return;
    if (H->LTAG == 1) { // If there is a root node attached
        FREE_TREE_RECURSIVE(H->LSON);
    }
    // Finally, free the head node itself
     // printf("Freeing head node\n"); // Debug print
    free(H);
}


/*
 Standard linear search - returns index or -1 if not found.
*/
int LOOK (int *list, int size, int key)
{
    int i;
    for (i = 0; i < size; i++)
        if (list[i] == key) return i;

    return -1; // Indicate not found
}

// --- Inorder Traversal Functions (Correct) ---
BinaryTreeNode *INSUC(BinaryTreeNode *alpha)
{
    BinaryTreeNode *beta = alpha->RSON;
    if (alpha->RTAG == 1){ // If RSON is a child link
        // Go to the leftmost node in the right subtree
        while (beta->LTAG == 1){ // Follow left child links
            beta = beta->LSON;
        }
    }
    // If RTAG is 0, RSON is already the inorder successor thread
    // If RTAG is 1, beta now points to the leftmost node (inorder successor)
    return beta;
}

BinaryTreeNode *INPRED (BinaryTreeNode *alpha)
{
    BinaryTreeNode *beta = alpha->LSON;
    if (alpha->LTAG == 1){ // If LSON is a child link
         // Go to the rightmost node in the left subtree
        while (beta->RTAG == 1){ // Follow right child links
            beta = beta->RSON;
        }
    }
     // If LTAG is 0, LSON is already the inorder predecessor thread
     // If LTAG is 1, beta now points to the rightmost node (inorder predecessor)
    return beta;
}

void INORDER_T (BinaryTreeNode *H)
{
    BinaryTreeNode *alpha = H; // Start from head
    while (1){
        alpha = INSUC(alpha); // Find next inorder successor
        if (alpha == H) return; // Traversed back to head, done
        else VISIT(alpha);
    }
}

// --- Preorder Traversal Functions (Correct) ---
BinaryTreeNode *PRESUC (BinaryTreeNode *alpha)
{
    if (alpha->LTAG == 1) { // If there's a left child, it's the preorder successor
        return alpha->LSON;
    } else { // No left child (LSON is a thread or points to head)
        // Follow right links (child or thread) until we find a node
        // whose right pointer is a child link, or we hit the head.
        BinaryTreeNode *beta = alpha;
        while (beta->RTAG == 0){ // While right pointer is a thread
            beta = beta->RSON;   // Follow the thread
            if (beta == alpha || beta->DATA == -1) return beta; // Avoid infinite loop or going past last node to head incorrectly. Let head handle termination.
                                                               // Using DATA == -1 check specific to head node
        }
        // Now beta->RTAG is 1, so beta->RSON points to the right child,
        // which is the preorder successor in this case.
        return beta->RSON;
    }
}

void PREORDER_T (BinaryTreeNode *H)
{
    BinaryTreeNode *alpha = H; // Start from head
    while (1){
        alpha = PRESUC(alpha); // Find next preorder successor
        if (alpha == H) return; // Traversed back to head, done
        else VISIT(alpha);
    }
}


// --- CORRECTED Postorder Traversal (Iterative using Stack) ---
void POSTORDER_T(BinaryTreeNode *H) {
    if (H == NULL || H->LTAG == 0) { // Check for NULL head or empty tree
        newline;
        return;
    }

    // Simple stack implementation (adjust size if needed)
    BinaryTreeNode* stack[100];
    int top = -1;

    BinaryTreeNode* current = H->LSON; // Start at the actual root
    BinaryTreeNode* last_visited = NULL;

    while (top > -1 || current != NULL) {
        if (current != NULL) {
            // Go as far left as possible
            stack[++top] = current;
            if (current->LTAG == 1) { // Only follow actual child links down
                current = current->LSON;
            } else {
                current = NULL; // Stop descent if it's a thread
            }
        } else {
            // Backtrack or process right subtree
            BinaryTreeNode *peek_node = stack[top]; // Node at top of stack

            // Check if right child exists (RTAG=1) and hasn't been visited yet
            if (peek_node->RTAG == 1 && last_visited != peek_node->RSON) {
                current = peek_node->RSON; // Descend into the right subtree
            } else {
                // Visit the node (either leaf or right subtree already processed)
                VISIT(peek_node);
                last_visited = peek_node; // Mark as visited
                top--;                    // Pop from stack
                current = NULL;           // Stay in "backtrack" mode
            }
        }
    }
    newline; // Print newline after traversal
}


// --- Main Function ---
int main() {
    BinaryTreeNode *H; // Pointer to the head node
    CREATE(&H);        // Create the threaded tree from input

    printf("Inorder Traversal:\n");
    INORDER_T(H);
    newline; // Add newline for separation

    printf("Preorder Traversal:\n");
    PREORDER_T(H);
    newline; // Add newline for separation

    printf("Postorder Traversal (Corrected):\n");
    POSTORDER_T(H); // Call the corrected iterative postorder
    // newline; // POSTORDER_T now prints its own newline

    // Free the allocated memory
    FREE_TREE(H);

    return 0;
}