#include <stdio.h>
#include <stdlib.h>

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
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        return;
    }
    newNode->vertex = dest;
    newNode->next = adjList[src];
    adjList[src] = newNode;
    inDegree[dest]++; // Update in-degree of destination vertex
}

void topologicalSort(int n) {
    Queue* q = initQueue();
    
    if (q == NULL) {
        return;
    }
    
    for (int i = 1; i <= n; i++) {
        if (inDegree[i] == 0) {
            enqueue(q, i);
        }
    }

    int count = 0;
    while (!isEmpty(q)) {
        int v = dequeue(q);
        printf("%d ", v);
        count++;

        Node* temp = adjList[v];
        while (temp) {
            int neighbor = temp->vertex;
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                enqueue(q, neighbor);
            }
            temp = temp->next;
        }
    }
    
    free(q);
}

int main() {
    int src;
    int dest;
    int n; 

    // Read the number of vertices
    scanf("%d", &n);

    // Initialize adjacency list and in-degree array
    for (int i = 1; i <= n; i++) {
        adjList[i] = NULL;
        inDegree[i] = 0;
    }

    while (1) {
        scanf("%d %d", &src, &dest);
        if (src == 0 && dest == 0) break;
        addEdge(src, dest);
    }

    topologicalSort(n);

}