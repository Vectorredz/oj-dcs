#ifndef ADJ_LIST_H
#define ADJ_LIST_H

#include <stdint.h>

// Struct to represent each edge in the graph
typedef struct edge {
    int node1;    // Start of the edge
    int node2;    // End of the edge
    int weight;   // Weight of the edge
} edge;

// Struct for each node in the adjacency list (a linked list node)
typedef struct list {
    int node;         // The destination vertex of an edge
    int weight;       // The weight of this edge
    struct list *next; // Pointer to the next node in the list
} list;

// Struct to represent the entire adjacency list of the graph
typedef struct adj_list {
    int n;           // Number of vertices
    list **adj;      // Array of pointers to linked lists (each representing edges for a vertex)
} adj_list;

adj_list *make_adj_list(int n, int e, edge *edges);

#endif