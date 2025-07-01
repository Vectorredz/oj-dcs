#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define k 100  
typedef char StackElemType;

typedef struct stack {
    int top;
    StackElemType *Stacks;
} Stack;
void InitStack(Stack *S) {
    S->top = -1;
    S->Stacks = (char *)malloc(k * sizeof(char));
}
void Push(Stack *S, StackElemType x) {
    if (S->top < k - 1) {
        S->top++;
        S->Stacks[S->top] = x;
    }
}
void Pop(Stack *S, StackElemType *x) {
    if (S->top >= 0) {
        *x = S->Stacks[S->top];
        S->top--;
    }
}
char *distribute(const char *e) {
    int len = strlen(e);
    char *result = malloc((len + 1) * sizeof(char));
    int res_i = 0;
    char signModifier = '+';  
    int valid = 0;            
    int i = 0;
    Stack S;
    InitStack(&S);
    while (e[i]) {
        if (e[i] == '+' || e[i] == '-') {
            if (valid) {
                result[res_i++] = (e[i] == '+') ? '-' : '+';
            } else {
                result[res_i++] = e[i];
            }
            signModifier = e[i]; 
        } else if (e[i] == '(') {
            Push(&S, signModifier);
            valid = (signModifier == '-');  
        } else if (e[i] == ')') {
            StackElemType x;
            Pop(&S, &x);  
            valid = (S.top != -1 && S.Stacks[S.top] == '-'); 
        } else {
            if (!(res_i > 0 && (result[res_i - 1] == '+' || result[res_i - 1] == '-') && e[i] == '+')) {
                result[res_i++] = e[i];
            }
        }
        i++;
    }
    result[res_i] = '\0';    
    return result;
}

int main() {
    char exp[] = "a-(-x+y+z)-(a-b)";
    char *ret = distribute(exp);
    printf("%s\n", ret);
    free(ret);  
    return 0;
}
