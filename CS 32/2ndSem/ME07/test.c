#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 10000

/*
> - next node
< - prev node
+ - add val of the node
- - subtract val of the node
. - print node
, - insert
[] - group of symbols

struct for instruction list
struct for machine list

*/
/*

*/

typedef struct node {
    char val;
    struct node *next;
    struct node *prev;
} Node;

typedef struct list {
    Node *head;
    int size;
    char instr[MAX];
} List;

Node *createNode() {
    Node *newNode = malloc(sizeof(Node));
    newNode->val = 0;
    newNode->next = newNode->prev = NULL;
    return newNode;
}

List *initList() {
    List *l = malloc(sizeof(List));
    l->head = createNode();
    return l;
}

    // traverse to the instruction
    // for (int i = 0; i < l->size; i++){
    //     printf("%c", l->instr[i]);
    // }

    /*
        0  <->  0 <-> 0 
    
    */

// preprocess brackets for better matching 

int preprocessBrackets(int len, char *instr, int *match) {
    int stack[MAX], top = -1;
    
    for (int i = 0; i < len; i++) {
        if (instr[i] == '[') {
            stack[++top] = i;
        } else if (instr[i] == ']') {
            if (top < 0) return 0;
            int openIdx = stack[top--];
            match[openIdx] = i;
            match[i] = openIdx; 
        }
    }
    
    return (top == -1);
}

Node *interpreter(List *l, int *data, int n) {
    Node *curr = l->head;
    int k = 0, i = 0;
    int match[MAX];

    if (!preprocessBrackets(l->size, l->instr, match)) {
        printf("UNCLOSED\n");
        return NULL;
    }

    while (i < l->size) {
        switch (l->instr[i]) {
            case ',':
                if (k >= n) {
                    printf("NO INPUT\n");
                    return NULL;
                }
                curr->val = data[k++];
                break;
            case '<':
                if (!curr->prev) {
                    Node *newNode = createNode();
                    curr->prev = newNode;
                    newNode->next = curr;
                    curr = newNode;
                    l->head = curr;
                } else {
                    curr = curr->prev;
                }
                break;
            case '>':
                if (!curr->next) {
                    Node *newNode = createNode();
                    curr->next = newNode;
                    newNode->prev = curr;
                    curr = newNode;
                } else {
                    curr = curr->next;
                }
                break;
            case '+':
                if (curr->val < 255) curr->val++;
                break;
            case '-':
                if (curr->val > 0) curr->val--;
                break;
            case '[':
                if (curr->val == 0) {
                    i = match[i];
                }
                break;
            case ']':
                if (curr->val != 0) {
                    i = match[i];
                }
                break;
            case '.':
                printf("%c", curr->val);
                break;
        }
        i++;
    }

    return l->head;
}

void display(Node *ret) {
    Node *curr = ret;

    while (curr->prev) {
        curr = curr->prev;
    }

    printf("\n");
    
    while (curr) {
        printf("%u", curr->val);
        if (curr->next) {
            printf(",");
        }
        curr = curr->next;
    }

    printf("\n");
}

int main() {
    int n, i = 0;
    scanf("%d", &n);

    if (n < 0) {
        printf("NO INPUT\n");
        return 0;
    }

    List *l = initList();
    unsigned int data[MAX];

    scanf("%s", l->instr);
    l->size = strlen(l->instr);

    while (i < n) {
        scanf("%u", &data[i]);
        i++;
    }

    Node *result = interpreter(l, data, n);
    if (result) display(result);
    
    return 0;
}
