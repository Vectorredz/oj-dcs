#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTICES 1000

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct Queue {
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

Node* adjList[MAX_VERTICES]; // Adjacency list
int inDegree[MAX_VERTICES];  // In-degree count array

// Initialize the queue
Queue* initQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    if (q == NULL) return NULL;
    q->front = -1;
    q->rear = -1;
    return q;
}

int isEmpty(Queue* q) {
    return q->front == -1;
}

// Enqueue a vertex
void enqueue(Queue* q, int value) {
    if (q->rear == MAX_VERTICES - 1) return;
    if (q->front == -1) q->front = 0;
    q->items[++q->rear] = value;
}

int dequeue(Queue* q) {
    if (isEmpty(q)) return -1;
    int item = q->items[q->front];
    if (q->front >= q->rear) q->front = q->rear = -1;
    else q->front++;
    return item;
}

// Add an edge to the adjacency list
void addEdge(int src, int dest) {
    if (src < 0 || src >= MAX_VERTICES || dest < 0 || dest >= MAX_VERTICES) return;
    
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) return;
    newNode->vertex = dest;
    newNode->next = adjList[src];
    adjList[src] = newNode;
    inDegree[dest]++; // Update in-degree of destination vertex
}

// from slides and kahn's algorithm
void topologicalSort(int n) {
    Queue* q = initQueue();
    int visited = 0;
    
    // Find all vertices with in-degree 0
    for (int i = 1; i <= n; i++) {
        if (inDegree[i] == 0) {
            enqueue(q, i);
        }
    }

    // decrement the in-degree
    while (!isEmpty(q)) {
        int v = dequeue(q);
        printf("%d ", v);
        visited++;

        Node* temp = adjList[v];
        while (temp != NULL) {
            int neighbor = temp->vertex;
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                enqueue(q, neighbor);
            }
            temp = temp->next;
        }
    }

    if (visited != n) {
        return;
    }
    
    free(q);
}

int main() {
    int src, dest, n;

    if (scanf("%d", &n) != 1 || n <= 0 || n >= MAX_VERTICES) return 0;

    memset(adjList, 0, sizeof(adjList));
    memset(inDegree, 0, sizeof(inDegree));

    // inputs for pair, so once encountered 0,0 break since it is the end of the list
    while (1) {
        if (scanf("%d %d", &src, &dest) != 2) {
            return 1;
        }
        if (src == 0 && dest == 0) break;
        if (src < 1 || src > n || dest < 1 || dest > n) {
            continue;
        }
        addEdge(src, dest);
    }

    topologicalSort(n);
}