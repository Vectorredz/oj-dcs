#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Stack {
    int capacity;
    int top;
    int *array;
} Stack;

// Create a stack with given capacity
Stack* createStack(int capacity) {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    s->capacity = capacity;
    s->top = -1;
    s->array = (int*)malloc(s->capacity * sizeof(int));
    return s;
}

// Check if the stack is empty
int isEmpty(Stack *s) {
    return s->top == -1;
}

// Check if the stack is full
int isFull(Stack *s) {
    return s->top == s->capacity - 1;
}

// Push an element onto the stack
void push(Stack *s, int disk) {
    if (isFull(s)) return;
    s->array[++(s->top)] = disk;
}

// Pop an element from the stack
int pop(Stack *s) {
    if (isEmpty(s)) return INT_MIN;
    return s->array[s->top--];
}

// Peek at the top element of the stack
int peek(Stack *s) {
    if (isEmpty(s)) return INT_MIN;
    return s->array[s->top];
}

// Move a disk from source to target stack
void moveDisk(Stack *source, Stack *target, char *sourceName, char *targetName) {
    int sourceTop = peek(source);
    int targetTop = peek(target);

    // Move from source to target if:
    // 1. Source is not empty, and
    // 2. Target is empty OR sourceTop <= targetTop
    if (!isEmpty(source) && (isEmpty(target) || sourceTop <= targetTop)) {
        push(target, pop(source));
        printf("Move disk %d from %s to %s\n", sourceTop, sourceName, targetName);
    }
    // Move from target to source if:
    // 1. Target is not empty, and
    // 2. Source is empty OR targetTop <= sourceTop
    else if (!isEmpty(target) && (isEmpty(source) || targetTop <= sourceTop)) {
        push(source, pop(target));
        printf("Move disk %d from %s to %s\n", targetTop, targetName, sourceName);
    }
}

// Perform the Tower of Hanoi moves
void TowerOfHanoi(int numDisks, Stack *source, Stack *target, Stack *auxiliary) {
    int totalMoves = (int)(pow(2, numDisks)) - 1;

    // Swap target and auxiliary for even number of disks
    if (numDisks % 2 == 0) {
        Stack *temp = target;
        target = auxiliary;
        auxiliary = temp;
    }

    for (int move = 1; move <= totalMoves; move++) {
        if (move % 3 == 1) {
            moveDisk(source, target, "source", "target");
        }
        else if (move % 3 == 2) {
            moveDisk(source, auxiliary, "source", "auxiliary");
        }
        else if (move % 3 == 0) {
            moveDisk(auxiliary, target, "auxiliary", "target");
        }
    }
}

int main() {
    int numDisks;
    printf("Enter the number of disks: ");
    scanf("%d", &numDisks);

    if (numDisks < 0) {
        printf("Number of disks cannot be negative.\n");
        return 0;
    }

    // Create stacks for source, target, and auxiliary
    Stack *source = createStack(numDisks);
    Stack *target = createStack(numDisks);
    Stack *auxiliary = createStack(numDisks);

    // Input disk sizes
    int *disks = (int*)malloc(numDisks * sizeof(int));
    printf("Enter the sizes of the disks (from bottom to top): ");
    for (int i = 0; i < numDisks; i++) {
        scanf("%d", &disks[i]);
    }

    // Initialize the source stack with disks (largest at the bottom)
    for (int i = numDisks - 1; i >= 0; i--) {
        push(source, disks[i]);
    }

    // Perform the Tower of Hanoi moves
    TowerOfHanoi(numDisks, source, target, auxiliary);

    // Print the final state of the target stack
    printf("Final state of the target stack (bottom to top): ");
    while (!isEmpty(target)) {
        printf("%d\n", pop(target));
    }
    printf("\n");

    // Free allocated memory
    free(disks);
    free(source->array);
    free(source);
    free(target->array);
    free(target);
    free(auxiliary->array);
    free(auxiliary);

    return 0;
}