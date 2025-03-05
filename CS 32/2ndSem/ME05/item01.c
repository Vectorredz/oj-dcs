#include <stdio.h>
#include <stdlib.h>
#define MAX 50
#define SIZE 100
#include <string.h>

typedef struct STACK{
    int top;
    int out_top;
    char *stack[MAX]; // website stack
    char *out_stack[MAX];
}Stack;

Stack *buildStack(){
    Stack *s = (Stack*)malloc(sizeof(Stack));
    s->top = -1;
    s->out_top = -1;
    return s;
}

void push(Stack *s, char *line){
    s->stack[++(s->top)] = line;
}

void pop(Stack *s){
    if (s->top > 0){
        s->stack[(s->top)--] = NULL;
    }
}

void operationStack(Stack *s, char *line){
    if (strcmp(line, "dump") == 0){
        s->out_stack[++s->out_top] = s->stack[s->top];
    }
    else if (strcmp(line, "back") == 0){
        pop(s);
    }
}

void inputChecker(Stack *s, char *line){
    line[strcspn(line, "\n")] = '\0';
    if (strcmp(line, "dump") == 0 || strcmp(line, "back") == 0){
        operationStack(s, line);
    }
    else {
        push(s, line);
    }
}

void resetStack(Stack *s){
    char *last_displayed = s->stack[s->top];
    while (s->top > 0){
        pop(s);
    }
    s->stack[s->top] = last_displayed;
}

int main(){
    // initialize the stack
    Stack *s = buildStack();

    unsigned int n; // number of testcases
    char line[50];

    scanf("%u", &n);
    if (n > 100) return 0; // invalid

    unsigned int c;

    unsigned int i = 0;
    scanf("%s", line);// first url
    push(s, strdup(line));

    while(i < n){
        scanf("%u", &c); // ask for the no. operations
        getchar();
        if (c > 10000) return 0;

        char buffer[c][50];

        unsigned int j = 0;

        while (j < c){
            scanf("%u", buffer[j]);
            inputChecker(s, buffer[j]);
            j++;
        }
        resetStack(s);
        i++;
    }

    for (int k = 0; k <= s->out_top; k++){
        printf("%s\n", s->out_stack[k]);
    }
}