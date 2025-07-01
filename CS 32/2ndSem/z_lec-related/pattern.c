#include <stdio.h>
#include <stdlib.h>
#define MAX 10000
#include <string.h>

typedef struct node{
    char val[MAX];
    struct node *next;
} Node;

typedef struct stack{
    int top; 
    Node *head;
} Stack;

Node *createNode(char val[MAX]){
    Node *new = malloc(sizeof(Node));
    strcpy(new->val, val);
    new->next = NULL;

    return new;
}

Stack *init(){
    Stack *s = malloc(sizeof(Stack));
    s->top = 0;
    s->head = NULL;
    return s;
}

void push(Stack *s, char *val){
    Node *new = createNode(val);
    if (s->top == 0 && !s->head){
        s->top++;
        s->head = new;
    }
    else{
        new->next = s->head;
        s->head = new;
        s->top++;
    }
}

void pop(Stack *s){
    Node *temp = s->head->next;
    s->head->next = NULL;
    free(s->head);
    s->head = temp;
}

char *peek(Stack *s){
    return s->head->val;
}

void display(Stack *s){
    Node *curr = s->head;
    while (curr){
        printf("%s -> ", curr->val);
        curr = curr->next;
    }
}

void pattern(Stack *s, char **k, char **p, int n){
    for (int i = 0; i < n-1; i++){
        if (strcmp(k[i], "c") == 0){
            if (strcmp(peek(s), k[i]) == 0){
                pop(s);
            }  
        }
    }
}

int main(){
    Stack *s = init();
    char *k[] = {"a", "c", "a"};
    char *p[3];

    int n = sizeof(k) / sizeof(k[0]);
    for (int i = 0; i < 3; i++) {
        p[i] = malloc(MAX * sizeof(char)); 
        strcpy(p[i], k[i]);
    }
    // push(s, p[0]);
    // printf("%s", s->head->val);
    pattern(s, p, k, n);
    display(s);

}