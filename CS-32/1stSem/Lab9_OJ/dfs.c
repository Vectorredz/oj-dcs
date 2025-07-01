#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 100

typedef struct Node{
    int vertex;
    struct Node *next;
} Node;

typedef struct Graph{
    int v;
    Node **adjLists;
    int *visited;
} Graph;

// create node

Node *createNode(int vertex){
    Node *newNode = malloc(sizeof(Node));
    newNode->vertex = vertex;
    newNode->next = NULL;
    return newNode;
}

// initialize a graph

Graph *createGraph(int vertices){
    Graph *graph = (malloc(sizeof(Graph)));
    graph->v = vertices;
    graph->adjLists = (malloc(vertices * sizeof(Node*)));
    graph->visited = (malloc(vertices * sizeof(int)));
    // init to null all heads

    for (int i = 0; i < vertices; i++){
        graph->adjLists[i] = NULL;
        graph->visited[i] = 0;
    }

    return graph;
}

void addEdge(Graph *graph, int u, int v){
    Node *newNode = createNode(v);
    newNode->next = graph->adjLists[u];
    graph->adjLists[u] = newNode;

    newNode = createNode(u);
    newNode->next = graph->adjLists[v];
    graph->adjLists[v] = newNode;

}

// Recursive DFS function
void dfs(Graph* graph, int vertex, int dest) {
    graph->visited[vertex] = 1;

    Node* temp = graph->adjLists[vertex];
    if (temp->vertex == dest){
        printf("%d %d ", vertex, temp->vertex);
        return;
    }

    while (temp) {
        int connectedVertex = temp->vertex;

        if (!graph->visited[connectedVertex]) {
            dfs(graph, connectedVertex, 4);
        }

        temp = temp->next;
    }
}

// Main function
int main() {
    int vertices = 5;

    Graph* graph = createGraph(vertices);

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);

    printf("valid path: \n");
    dfs(graph, 0, 4);

    // Free allocated memory
    for (int i = 0; i < vertices; i++) {
        Node* temp = graph->adjLists[i];
        while (temp) {
            Node* toFree = temp;
            temp = temp->next;
            free(toFree);
        }
    }
    free(graph->adjLists);
    free(graph->visited);
    free(graph);

    return 0;
}
