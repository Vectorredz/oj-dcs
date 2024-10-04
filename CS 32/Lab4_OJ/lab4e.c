#include <stdlib.h>
#include "all_nearest_smaller.h"
typedef int StackType;
typedef struct stack {
    int top; StackType *Stacks;
} Stack;
void Init(Stack *S){
    S->top = -1; S->Stacks = malloc(1000000 * sizeof(int));
}
int Push(Stack *S, StackType x){
    if (S->top < 1000000){
        S->Stacks[++S->top] = x;
    }
}
int Pop(Stack *S, StackType *x){
    if (S->top != -1){
        *x = S->Stacks[S->top]; S->top--;
    }
}
int *helper(int n, int64 *s, Stack *S){
    int *result = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++){
        while (S->top != -1 && s[S->Stacks[S->top]] >= s[i]){
            StackType y;
            Pop(S, &y);
        }
        if (S->top == -1){
            result[i] = -1;
        }
        else {
            result[i] = S->Stacks[S->top];
        }
        Push(S, i);
    }
    return result;
}
int *all_nearest_smaller(int n, int64 *s){
    Stack S; Init(&S);
    return helper(n, s, &S);
}