#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define k 101
typedef char StackElemType;

typedef struct stack {
    int top;
    StackElemType *Stacks;
} Stack;

void InitStack(Stack *S) {
    S->top = -1;
    S->Stacks = (char*)malloc(k * sizeof(char));
}

int IsEmpty(Stack *S) {
    return S->top == -1;
}

void Push(Stack *S, StackElemType x) {
    if (S->top < k - 1) { // Check for stack overflow
        S->Stacks[++S->top] = x;
    }
}

int Pop(Stack *S, StackElemType *x) {
    if (!IsEmpty(S)) {
        *x = S->Stacks[S->top--];
        return 1; // Pop successful
    }
    return 0; // Stack is empty
}

char *distribute(const char *e) {
    Stack S;
    InitStack(&S);
    int len = strlen(e);
    char currSign = '+';
    char *result = (char*)malloc((2 * len) * sizeof(char)); // Allocate enough space
    int index = 0;

    for (int i = 0; i < len; i++) {
        if (e[i] == '+' || e[i] == '-') {
            currSign = e[i];
        } else if (e[i] == '(') {
            // Push the current sign onto the stack
            Push(&S, currSign);
            i++;
            while (e[i] != ')') {
                if (e[i] == '+' || e[i] == '-') {
                    if (currSign == '-') {
                        // Flip the sign
                        char flipped = (e[i] == '-') ? '+' : '-';
                        result[index++] = flipped; // Add flipped sign to result
                    } else {
                        result[index++] = currSign;
                        result[index++] = e[i]; // Add the sign as is
                    }
                } else {
                    result[index++] = e[i]; // Add variable
                }
                i++;
            }
        } else {
            result[index++] = e[i]; // Regular character
        }
    }
    result[index] = '\0'; // Null-terminate the result

    // Clean up
    free(S.Stacks);
    return result; // Return the result
}

int main() {
    char exp[] = "a-(-x+y+z)-(a-b)";
    char *result = distribute(exp);
    printf("Distributed expression: %s\n", result);
    free(result); // Free the result after use
    return 0;
}
