#include <stdlib.h>
#include <string.h>
#include "distribute.h"
typedef char StackElemType;
typedef struct stack {
    int top;
    StackElemType *Stacks;
} Stack;

void InitStack(Stack *S) {
    S->top = -1;
    S->Stacks = (StackElemType*)malloc(100 * sizeof(StackElemType)); 
}

void Push(Stack *S, StackElemType x) {
    S->Stacks[++S->top] = x;  
}

void Pop(Stack *S, StackElemType *x) {
    if (S->top == -1) return;  
    *x = S->Stacks[S->top--];  
}

char *distribute(const char *e) {
    char *result = (char*)malloc(1000000 * sizeof(char));
    char currSign;
    char modifier;
    char newSign;
    int index = 0;
    
    Stack S;
    InitStack(&S);
    
    for (int i = 0; e[i]; i++) {
        if (e[i] == '(') {
            currSign = (i == 0 || e[i-1] == '+') ? '+' : '-';
            modifier = (S.top == -1) ? '+' : S.Stacks[S.top];
            newSign = (currSign == modifier) ? '+' : '-';
            Push(&S, newSign);
        } else if (e[i] == ')') {
            StackElemType x;
            Pop(&S, &x);
        } else if (e[i] == '-' || e[i] == '+') {
            modifier = (S.top == -1) ? '+' : S.Stacks[S.top];
            newSign = (e[i] == modifier) ? '+' : '-';
            result[index++] = newSign;
        } else {
            result[index++] = e[i];
        }
    }
    result[index] = '\0';
    return result;
}
