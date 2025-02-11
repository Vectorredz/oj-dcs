#include "relief.h"
#include <stdlib.h>
#include <stdbool.h>

#define n 300000

typedef struct node{
    int k_i; // k-count
    int s_i; // s-count
} node;

typedef struct donations{
    int k; // k-type of items
    int r; // r-number of items
    node **curr; 
    node **target;
} Donasyon;


// initialize every property of struct donations
Donasyon *init(int k, int r, const int *b){
    Donasyon *d = malloc(sizeof(Donasyon));
    d->k = k;
    d->r = r;
    d->curr = malloc(n * sizeof(node*)); // curr dictionary
    d->target = malloc(n * sizeof(node*)); // target dictionary

    // init current 

    for (int i = 0; i < k; i++){
        d->curr[i] = malloc(sizeof(node));
        d->curr[i]->k_i = i;
        d->curr[i]->s_i = 0; // initializes to 0 each values
    }

    // init target
    for (int i = 0; i < k; i++){
        d->target[i] = malloc(sizeof(node));
        d->target[i]->k_i = i;
        d->target[i]->s_i = 0; 
        for (int j = 0; j < r; j++){
            if (d->target[i]->k_i == b[j]){
                d->target[i]->s_i++;
            }
        }
    }
    return d;
}

bool all(struct donations *d){
    bool flag = false;
    for (int i = 0; i < d->k; i++){
        if (d->curr[i]->s_i < d->target[i]->s_i){
            return false;
        }
    }
    return true;
}

bool donate(struct donations *d, int d_i){
    if (d_i < 0 || d_i >= d->k){
        return false;
    }
    // update bool
    d->curr[d_i]->s_i++;

    // check if current numbers are enough to make a relief good
    if (all(d)) {
        // Deduct the required items from `curr` for each type
        for (int i = 0; i < d->k; i++) {
            d->curr[i]->s_i -= d->target[i]->s_i;
        }
        return true;
    }
    return false;
}