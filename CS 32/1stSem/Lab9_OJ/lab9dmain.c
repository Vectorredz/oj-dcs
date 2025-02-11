#include <stdio.h>
#include <stdlib.h>
#include "stroll.h"

#define k 200000

typedef struct PATH {
    int *parks;
    int length;
} PATH;

typedef struct list {
    int node;
    struct list *next;
} list;

typedef struct adj_list {
    int n;
    list **adj;
} adj_list;

adj_list *make_adj_list(int n, int e, road *roads) {
    adj_list *result = malloc(sizeof(adj_list));
    result->n = n;
    result->adj = malloc(n * sizeof(list*));

    for (int i = 0; i < n; i++) {
        result->adj[i] = NULL;
    }

    for (int i = 0; i < e; i++) {
        int vertex_1 = roads[i].start;
        int vertex_2 = roads[i].end;
        list *nextVertex2 = malloc(sizeof(list));
        nextVertex2->node = vertex_2;
        nextVertex2->next = result->adj[vertex_1];
        result->adj[vertex_1] = nextVertex2;
    }
    return result;
}

void visit(int park) {
    printf("Visiting park %d\n", park);
}

void update_best_path(PATH *best_path, PATH *current_path) {
    if (current_path->length > best_path->length) {
        best_path->length = current_path->length;
        for (int i = 0; i < current_path->length; i++) {
            best_path->parks[i] = current_path->parks[i];
        }
    }
}

void dfs(adj_list *graph, int node, int *visited, PATH *current_path, PATH *best_path, int dest) {
    if (node == dest) {
        update_best_path(best_path, current_path);

        for (int i = 0; i < current_path->length; i++) {
            visit(current_path->parks[i]);
        }
        return;
    }

    visited[node] = 1;
    current_path->parks[current_path->length] = node;
    current_path->length++;

    list *curr = graph->adj[node];
    while (curr != NULL) {
        if (!visited[curr->node]) {
            dfs(graph, curr->node, visited, current_path, best_path, dest);
        }
        curr = curr->next;
    }

    visited[node] = 0;
    current_path->length--;
}

void find_leisurely_path(int n, int r, road *roads) {
    adj_list *graph = make_adj_list(n, r, roads);
    int visited[n];
    for (int i = 0; i < n; i++) {
        visited[i] = 0;
    }

    PATH current_path = { malloc(n * sizeof(int)), 0 };
    PATH best_path = { malloc(n * sizeof(int)), 0 };

    dfs(graph, 0, visited, &current_path, &best_path, 1);

    printf("Longest leisurely path from park 0 to park 1: ");
    for (int i = 0; i < best_path.length; i++) {
        printf("%d ", best_path.parks[i]);
    }
    printf("\n");

    free(current_path.parks);
    free(best_path.parks);
}

int main() {
    road roads1[] = {{0, 1}};
    int n1 = 2;
    int e1 = 1;
    printf("Test Case 1:\n");
    find_leisurely_path(n1, e1, roads1);
    printf("\n");

    road roads2[] = {{0, 1}, {0, 2}, {2, 1}};
    int n2 = 3;
    int e2 = 3;
    printf("Test Case 2:\n");
    find_leisurely_path(n2, e2, roads2);
    printf("\n");

    road roads3[] = {{0, 1}, {0, 2}, {2, 3}, {3, 4}, {4, 1}};
    int n3 = 5;
    int e3 = 5;
    printf("Test Case 3:\n");
    find_leisurely_path(n3, e3, roads3);
    printf("\n");

    road roads4[] = {{2, 3}, {3, 4}, {4, 5}};
    int n4 = 6;
    int e4 = 3;
    printf("Test Case 4:\n");
    find_leisurely_path(n4, e4, roads4);
    printf("\n");

    road roads5[] = {{0, 1}, {1, 2}, {2, 0}, {2, 3}, {3, 1}};
    int n5 = 4;
    int e5 = 5;
    printf("Test Case 5:\n");
    find_leisurely_path(n5, e5, roads5);
    printf("\n");

    return 0;
}
