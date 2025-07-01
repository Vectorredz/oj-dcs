#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 50

typedef struct node {
    char stack[MAX];  // stack of webpages
    struct node *next;
} Node;

typedef struct list {
    int size;
    Node *head;
} List;

List *build() {
    List *l = (List*)malloc(sizeof(List));
    l->head = NULL;
    l->size = 0;  
    return l;
}

Node *newNode(char *webpage) {
    Node *node = (Node *)malloc(sizeof(Node));
    strncpy(node->stack, webpage, MAX - 1);  
    node->stack[MAX - 1] = '\0'; 
    node->next = NULL;
    return node;
}

void push(List *l, char *webpage) {
    Node *node = newNode(webpage);
    node->next = l->head;
    l->head = node;
    l->size++;  // Increment size
}

void pop(List *l){
    if (l->head->next == NULL) return; // dont pop the single element

    Node *prev = l->head->next;
    Node *curr = prev->next;

    l->head = NULL;
    free(l->head);

    l->head = prev;
    prev->next = curr;

}

void printList(List *l, List *sort) {
    Node *curr = l->head;
    while (curr) {
        push(sort,   curr->stack);
        pop(l);
        curr = curr->next;
    }

    Node *ret = sort->head;
    while (ret) {
        printf("%s\n", ret->stack);
        ret = ret->next;
    }
}

void inputSelector(List *l,  List *op, char *webpage){
    webpage[strcspn(webpage, "\n")] = '\0';
    if (strcmp(webpage, "dump") == 0 || strcmp(webpage, "back") == 0 ){
        if (strcmp(webpage, "back") == 0){
            pop(l);
        }
        else {
            push(op, l->head->stack);
        }
    }
    else {
        push(l, webpage);
    }
}

void reset(List *l, List *op){
    Node *curr = l->head;
    Node *temp = l->head;
    while (curr->next){
        pop(l);
        curr = curr->next;
    }
    
    curr = temp;
    l->head = curr;
    l->head->next = NULL;
    
}

int main() {
    List *website = build(); // webpages stack
    List *operation = build(); // store the webpages in a stck
    List *sorted = build();
    int N;
    int C;

    scanf("%d", &N);
    getchar();

    if (N > 100) return 0;

    char buffer[MAX];

    fgets(buffer, MAX, stdin);
    inputSelector(website, operation, buffer);

    int i = 0;
    while (i < N){
        scanf("%d", &C);
        getchar();

        if (C > 10000) return 0;

        int j = 0;

        while (j < C)
        {
            fgets(buffer, MAX, stdin);
            inputSelector(website, operation, buffer);
            j++;
        }
        reset(website, operation);
        i++;
    }
    printList(operation, sorted);

    return 0;
}