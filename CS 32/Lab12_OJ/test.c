#include <stdio.h>
#include <stdlib.h>


// count 
typedef struct node{
    int k_i;
} node;

typedef struct dictionary{
    // list of nodes
    node **nodes;

} dict;

int main(){
    int n = 10;
    dict *d = malloc(sizeof(dict) * n);
    node *key1 = malloc(sizeof(node));
    key1->k_i = 1;
    key1->k_i++;
    d->nodes[0] = key1;


    printf("%d", d->nodes[0]->k_i);


}