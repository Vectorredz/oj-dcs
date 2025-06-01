#include <stdio.h>
#include <stdlib.h>

typedef struct queueNode
{
    int val;
    struct queueNode *next;
} QueueNode;

typedef struct queue{
    QueueNode *front;
    QueueNode *rear;
} Queue;

QueueNode *createNode(int val){
    QueueNode *new = malloc(sizeof(QueueNode));
    new->next = NULL;
    new->val = val;

    return new;
}

void enqueue(Queue *q, int val){
    QueueNode *new = createNode(val);
    if (!q->front && !q->rear){
        q->rear = q->front = new;
    }
    q->rear->next = new;
    q->rear = new;
    
}

void dequeue(Queue *q){
    QueueNode *temp = q->front->next;
    q->front->next = NULL;
    q->front = NULL;
    q->front = temp;

}

void display(Queue *q){
    QueueNode *curr = q->front;
    while (curr){
        printf("%d -> ", curr->val);
        curr = curr->next;
    }
    printf("\n");
}

int main(){
    Queue *q = malloc(sizeof(Queue));
    q->front = q->rear = NULL;


    enqueue(q, 1);
    enqueue(q, 2);
    enqueue(q, 3);
    display(q);
    dequeue(q);
    display(q);
}