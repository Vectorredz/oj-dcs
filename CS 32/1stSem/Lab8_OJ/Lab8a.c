#include <stdio.h>
#include <stdlib.h>
#include "adj_list.h"
#define k 1000

adj_list *make_adj_list(int n, int e, edge *edges){
    if (n <= 0 && e <= 0){
        return NULL;
    }
    adj_list *result = malloc(sizeof(adj_list));
    result->n = n;
    result->adj = malloc(n * sizeof(list*));

    for (int i = 0; i < n; i++){
        result->adj[i] = NULL;
    }

    for (int i = 0; i < e; i++){
        int vertex_1 = edges[i].node1;
        int vertex_2 = edges[i].node2;
        int weight = edges[i].weight;
        if (edges[i].node1 != edges[i].node2){
            list *nextVertex = malloc(sizeof(list));
            nextVertex->node = vertex_1;
            nextVertex->weight = weight;
            nextVertex->next = result->adj[vertex_2];
            result->adj[vertex_2] = nextVertex;
            list *nextVertex2 = malloc(sizeof(list));
            nextVertex2->node = vertex_2;
            nextVertex2->weight = weight;
            nextVertex2->next = result->adj[vertex_1];
            result->adj[vertex_1] = nextVertex2;
        }
        else {
            list *nextVertex2 = malloc(sizeof(list));
            nextVertex2->node = vertex_2;
            nextVertex2->weight = weight;
            nextVertex2->next = result->adj[vertex_1];
            result->adj[vertex_1] = nextVertex2;
        }
    }
    return result;
}

void print_adj_list(adj_list *graph) {
    for (int i = 0; i < graph->n; i++) {
        printf("%d: ", i);
        list *curr = graph->adj[i];
        while (curr) {
            printf("{%d, %d}", curr->node, curr->weight);
            curr = curr->next;
        }
        printf("\n");
    }
}

int main(){
    // edges : (0, 1; 4), (0, 2; 1), (2, 1; 3)
    // initialize edges
    edge edges[] = {{0, 1, 3}, {1, 2, 4}};  // Only vertices 0, 1, and 2 are connected
    int n = 5, e = 2;
    adj_list *ret = make_adj_list(n, e, edges);



    print_adj_list(ret);
}