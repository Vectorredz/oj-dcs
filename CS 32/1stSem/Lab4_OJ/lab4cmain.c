#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "distribute.h"
typedef int StackElemType;
typedef struct stack {
    int top; StackElemType *Stacks;
} Stack;
void InitStack(Stack *S){
    S->top = -1; S->Stacks = (int*)malloc(1000000 * sizeof(int));
}
int Push(Stack *S, StackElemType x){
    S->top++;S->Stacks[S->top] = x;
}
int Pop(Stack *S, StackElemType *x){
    *x = S->Stacks[S->top]; S->top--;
}
char *distribute(const char *e){
    size_t n = strlen(e);
    char *result = (char*)malloc(100000 * sizeof(char));
    char currSign;
    char modifier;
    char newSign;
    int index = 0;
    Stack S;
    InitStack(&S);
    for (int i = 0; i < n; i++)
    {
        if (e[i] == '('){
            currSign = (i == 0 || e[i] == '+' || e[i] == '(') ? '+' : '-';
            modifier = (S.top == -1) ? '+' : (S.Stacks[S.top]);
            newSign = (currSign == modifier) ? '+' : '-';
            Push(&S, newSign);
        }
        else if (e[i] == ')'){
            StackElemType x;
            Pop(&S, &x);
        }
        else if ((e[i] == '-' || e[i] == '+') && e[i+1] != '('){
            modifier = (S.top == -1) ? '+' : (S.Stacks[S.top]);
            newSign = (e[i] == modifier) ? '+' : '-';
            result[index++] = newSign;
        }
        else {
            result[index++] = e[i];
        }
        result[index] = '\0';
    }
    return result;
}
int main() {
    char *result = distribute("a+((x+y)-(w+z-a-(b+x)))");
    printf("%s\n", result);  
    return 0;
}
