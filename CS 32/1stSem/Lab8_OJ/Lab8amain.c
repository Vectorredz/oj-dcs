#include <stdlib.h>
#include "adj_list.h"
adj_list *make_adj_list(int n, int e, edge *edges){
    if (n <= 0 || e < 0){
        return NULL;}
    adj_list *res = malloc(sizeof(adj_list)); res->n = n; res->adj = malloc(n * sizeof(list*));
    if (!res) { 
        return NULL; }
    for (int i = 0; i < n; i++){
        res->adj[i] = NULL;}
    for (int i = 0; i < e; i++){
        int u1 = edges[i].node1; int u2 = edges[i].node2; int weight = edges[i].weight;
        list *v1 = malloc(sizeof(list));
        if (!(v1)){
            return NULL;}
        v1->node = u2; v1->weight = weight; v1->next = res->adj[u1]; res->adj[u1] = v1;
        list *v2 = malloc(sizeof(list));
        if (!(v2)){
            return NULL;}
        v2->node = u1; v2->weight = weight; v2->next = res->adj[u2]; res->adj[u2] = v2;
    }
    return res;
}