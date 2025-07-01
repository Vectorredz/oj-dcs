#include <stdio.h>
#include "dominions.h"
#include <stdlib.h>
typedef int StackElemType;
typedef struct {
    int top;
    StackElemType *Stacks;
} Stack;
void InitStack(Stack *S, int n) {
    S->top = -1;
    S->Stacks = (int*)malloc(n * sizeof(int));
}
void Push(Stack *S, StackElemType x) {
    S->top++;
    S->Stacks[S->top] = x;
}
void Pop(Stack *S, StackElemType *x) {
    *x = S->Stacks[S->top];
    S->top--;
}
int64 *helper(int n, int64 *h, Stack *S)
{
    int64 *result = (int64 *)malloc(n * sizeof(int64));
    int64 *left_count = (int64 *)malloc(n * sizeof(int64));
    int64 *right_count = (int64 *)malloc(n * sizeof(int64));
    InitStack(S, n);
    for (int i = 0; i < n ; i++){
        while (S->top != -1 && h[i] >= h[S->Stacks[S->top]]){
            StackElemType x;
            Pop(S, &x);
        }
        if (S->top == -1){
            left_count[i] = i;
        }
        else {
            left_count[i] = i - S->Stacks[S->top] - 1;
        }
        Push(S, i);
    }
    S->top = -1;
    for (int i = n - 1; i >= 0; i--){
        while (S->top != -1 && h[i] >= h[S->Stacks[S->top]]){
            StackElemType x;
            Pop(S, &x);
        }
        if (S->top == -1){
            right_count[i] =n - i - 1;
        }
        else {
            right_count[i] = S->Stacks[S->top] - i - 1;
        }
        Push(S, i);
    }
    for (int i = 0; i < n; i++) {
        result[i] = right_count[i] + left_count[i] + 1;
    }
    return result;
}
int64 *dominions(int n, int64 *h) {
    Stack S;
    helper(n, h, &S);
}


int main()
{
    Stack S; 
    InitStack(&S, 12);
    int64 list[] = {2,6,4,5,7,5,1,3,1,1,0,6};
    int64 *ret = dominions(12, list);
    for (int i = 0; i < 12; i++)
    {
        printf("%lld ", ret[i]);
    }

}
