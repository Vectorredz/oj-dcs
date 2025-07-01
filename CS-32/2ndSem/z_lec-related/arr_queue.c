#include <stdio.h>
#include <stdlib.h>
#define MAX 10

typedef struct Queue{
    int *array;
    int front;
    int rear;
} Queue;

void enqueue(Queue *q, int x){
    if (q->front == -1 && q->rear == -1){ // no elements in queue
        q->front++;
        q->rear++;
        q->array[q->front] = x; // front = 0;
    }  
    else {
        q->rear++; // rear = k
        q->array[q->rear] = x;
    }
}

void dequeue(Queue *q){
    q->array[q->front++] = -1;
}

void display(Queue *q){
    for (int i = q->front; i <= q->rear; i++){
        printf("%d -> ", q->array[i]);
    }
    printf("\n");
}

int main(){
    Queue *q = malloc(sizeof(Queue));
    q->front = q->rear = -1;
    q->array = malloc(sizeof(int) * MAX);
    enqueue(q, 1);
    enqueue(q, 2);
    enqueue(q, 3);
    enqueue(q, 4);
    display(q);
    dequeue(q);
    display(q);

}