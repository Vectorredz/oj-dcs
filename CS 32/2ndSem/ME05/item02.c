#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Stack {
    int capacity;
    int top;
    int temp_top;
    int *array;
    int *temp;
} Stack;

Stack* createStack(int capacity) {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    s->capacity = capacity;
    s->top = -1;
    s->temp_top = -1;
    s->array = (int*)malloc(s->capacity * sizeof(int));
    s->temp = (int*)malloc(s->capacity * sizeof(int));
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

void push_temp( Stack *s, int disk) {
    if (s->temp_top == s->capacity - 1) return;
    s->temp[++(s->temp_top)] = disk;
}

int pop( Stack *s) {
    if (s->top == -1) return INT_MIN;
    return s->array[s->top--];
}

int pop_temp( Stack *s) {
    if (s->temp_top == -1) return INT_MIN;
    return s->temp[s->temp_top--];
}
// Moving from one pole to another void 


// same element 
void moveDisks(Stack *src, Stack *dest) {
    int srcTopDisk = pop(src);
    int destTopDisk = pop(dest);

    if (srcTopDisk == INT_MIN && destTopDisk == INT_MIN) return;

    if (srcTopDisk == INT_MIN) {
        push(src, destTopDisk);
    }

    else if (destTopDisk == INT_MIN) {
        push(dest, srcTopDisk);
    }

    else if (srcTopDisk > destTopDisk) {
        push(src, srcTopDisk);
        push(src, destTopDisk);
    }

    else if (srcTopDisk < destTopDisk){
        push(dest, destTopDisk);
        push(dest, srcTopDisk);
    }

    else if (srcTopDisk == destTopDisk){
        push(dest, destTopDisk);
        push(dest, srcTopDisk);
        
    }
}

void hanoi(int numDisks, Stack *sorted_s, Stack *src, Stack *aux, Stack *dest) {

    int totalMoves = (int)((pow(2, numDisks)) - 1); // 2^n - 1

    // Swap aux and dest for even numDisks
    // if (numDisks % 2 == 0) {
    //     Stack *temp = aux;
    //     aux = dest;
    //     dest = temp;
    // }

    // Push all disks onto the source stack (largest disk at the bottom)
    // for (int i = sorted_s->top; i > 0; i--){
    //     push(src, sorted_s->array[i]);
    // }

    for (int i = 0; i <= sorted_s->top; i++){
        push(src, sorted_s->array[i]);
    }

    // Perform the moves
    for (int i = 1; i <= totalMoves; i++) {
        if (dest->top == sorted_s->capacity - 1) break;
        if (i % 3 == 1) moveDisks(src, dest);
        else if (i % 3 == 2) moveDisks(src, aux);
        else if (i % 3 == 0) moveDisks(aux, dest);
    }
}

// do monotonic stack for sorting
void monotonicStack(Stack *s, Stack *sorted_s){

    int curr = pop(s);
    if (sorted_s->top == -1){
        push(sorted_s, curr); // push the top element
        // printf("%d", sorted_s->array[sorted_s->top]);
    }

    while (s->top != -1){ // as long as the original stack has elements
        curr = pop(s);
        int peeked = peek(sorted_s);
        if (peeked >= curr){
            push(sorted_s, curr);
        }
        else {
            // pop everything
            while (curr > peek(sorted_s) && sorted_s->top != -1){
                // printf("popped\n");
                int popped = pop(sorted_s);
                push_temp(sorted_s, popped);
            }
            push(sorted_s, curr);
            while (sorted_s->temp_top > -1){
                int popped = pop_temp(sorted_s);
                push(sorted_s, popped); // final stack
            }
        }
    }
}

int main() {
    int n;

    scanf("%d", &n);

    if (n < 0) return 0;

    int *disks = malloc(n * sizeof(int));

    Stack *s = createStack(n);
    Stack *sorted_s = createStack(n);
    Stack *src = createStack(n);
    Stack *aux = createStack(n);
    Stack *dest = createStack(n);

    int j = 0;

    while (j < n){
        scanf("%d", &disks[j]);
        j++;
    }
    
    for (int i = 0; i < n; i++){
        push(s, disks[i]);
    }

    monotonicStack(s, sorted_s);

    for (int i = sorted_s->top; i >= 0; i--){
        printf("%d\n", sorted_s->array[i]);
    }

    // hanoi(n, sorted_s, src, aux, dest);

    // for (int i = dest->top; i >= 0; i--){
    //     printf("%d\n", dest->array[i]);
    // }

}