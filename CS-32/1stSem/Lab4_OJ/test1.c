#include "distribute.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct stack {
    int top;
    char *Stack;
} Stack;

void InitStack(Stack *S) {
    S->top = -1;
    S->Stack = malloc(1000000 * sizeof(char));
}

int isEmpty(Stack *S) {
    return S->top == -1;
}

void Push(Stack *S, char x) {
    if (S->top < 1000000) {
        S->Stack[++S->top] = x;
    }
}

void Pop(Stack *S) {
    if (!isEmpty(S)) {
        S->top--;
    }
}

char *distribute(const char *e) {
    int no_paren_count = 0, index = 0, result_index = 0;
    char operator = '0';
    char to_distribute = 0;

    while (e[index]) {
        if (e[index] != ')' && e[index] != '(') {
            no_paren_count++;
        }
        index++;
    }

    Stack S;
    InitStack(&S);
    char *result = malloc((no_paren_count + 1) * sizeof(char));
    index = 0;

    while (e[index]) {
        if (e[index] == '+' || e[index] == '-') {
            if (to_distribute) {
                if (e[index] == '+') {
                    result[result_index] = '-';
                } else if (e[index] == '-') {
                    result[result_index] = '+';
                }
                operator = result[result_index];
            } else {
                result[result_index] = e[index];
                operator = e[index];
            }
            result_index++;
        } else if (e[index] == '(') {
            to_distribute = (operator == '-');
            Push(&S, '(');
        } else if (e[index] == ')') {
            if (to_distribute) {
                Pop(&S);
                if (isEmpty(&S)) {
                    to_distribute = 0;
                }
            }
        } else {
            result[result_index++] = e[index];
        }
        index++;
    }
    result[result_index] = '\0';
    free(S.Stack);
    return result;
}

int main() {
    char exp[] = "a-(-x+y+z)-(a-b)";
    char *ret = distribute(exp);
    printf("%s\n", ret);
    free(ret);  // Free the result memory
    return 0;
}