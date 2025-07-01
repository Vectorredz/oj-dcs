#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Stack {
    int capacity;
    int top;
    int *array;
} Stack;

Stack* createStack(int capacity) {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    s->capacity = capacity;
    s->top = -1;
    s->array = (int*)malloc(s->capacity * sizeof(int));
    return s;
}

int peek(Stack *s) {
    if (s->top == -1) return INT_MIN;
    return s->array[s->top];
}

void push( Stack *s, int disk) {
    if (s->top == s->capacity - 1) return;
    s->array[++(s->top)] = disk;
}

int pop( Stack *s) {
    if (s->top == -1) return INT_MIN;
    return s->array[s->top--];
}

// do monotonic stack for sorting
void monotonicStack(Stack *src, Stack *dest, Stack *aux){

    int curr = pop(src);
    if (dest->top == -1){
        push(dest, curr); 
    }

    while (src->top != -1){ // as long as the original stack has elements
        curr = pop(src);
        int peeked = peek(dest);
        if (peeked >= curr){
            push(dest, curr);
        }
        else {
            // pop everything
            while (curr > peek(dest) && dest->top != -1){
                int popped = pop(dest);
                push(aux, poppedS);
            }
            push(dest, curr);
            while (aux->top > -1){
                int popped = pop(aux);
                push(dest, popped); // final stack
            }
        }
    }
}

int main() {
    int n;

    scanf("%d", &n);

    if (n < 0) return 0;

    int *disks = malloc(n * sizeof(int));

    Stack *src = createStack(n);
    Stack *dest= createStack(n);
    Stack *aux = createStack(n);

    int j = 0;

    while (j < n){
        scanf("%d", &disks[j]);
        j++;
    }
    
    for (int i = n-1; i >= 0; i--){
        push(src, disks[i]);
    }

    monotonicStack(src, dest, aux);

    for (int i = dest->top; i >= 0; i--){
        printf("%d\n", dest->array[i]);
    }
}