#include <stdio.h>
#include <stdlib.h>
#include "all_nearest_smaller.h"
#define k 101
typedef int StackElemType;
typedef struct stack {
    int top; StackElemType *Stacks;
} Stack;
void InitStack(Stack *S){
    S->top = -1; S->Stacks = (int*)malloc(k * sizeof(int));
}
int Push(Stack *S, StackElemType x){
    S->top++;S->Stacks[S->top] = x;
}
int Pop(Stack *S, StackElemType *x){
    *x = S->Stacks[S->top]; S->top--;
}
int *helper(int n, int64 *s, Stack *S){
    int *nearestSmaller = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++){
        while (S->top != -1 && s[S->Stacks[S->top]] >= s[i]){
            StackElemType x;
            Pop(S, &x);
        }
        if (S->top == -1){
            nearestSmaller[i] = -1;
        }
        else{
            nearestSmaller[i] = S->Stacks[S->top];
        }
        Push(S, i);
    }
    return nearestSmaller;
}
int *all_nearest_smaller(int n, int64 *s){
    Stack S; InitStack(&S);
    // int *ret = helper(n, s, &S);
    return helper(n, s, &S);
}
int main()
{
    int64 list[] = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    int n = sizeof(list) / sizeof(list[0]);

    int *ret = all_nearest_smaller(n, list);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", ret[i]);
    }
    printf("\n");

    return 0;
}
