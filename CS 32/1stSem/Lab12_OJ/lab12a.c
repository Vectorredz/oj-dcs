#include "relief.h"
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>

#define n 1000

#define VERIFY(b) do {\
    fprintf(stderr, "verifying: " #b "\n");\
    bool _b = (b);\
    if (!_b) {\
        fprintf(stderr, "verification failed!\n");\
        exit(1);\
    }\
} while (0)

// create donation 
// create init function
// create donations

typedef struct node{
    int k_i;
    int s_i;
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
    d->curr = malloc(n * sizeof(node*)); // dictionary
    d->target = malloc(n * sizeof(node*));

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

    // check if current numbers are enough to make
    if (all(d)) {
        // Deduct the required items from `curr` for each type
        for (int i = 0; i < d->k; i++) {
            d->curr[i]->s_i -= d->target[i]->s_i;
        }
        return true;
    }
    return false;
}


int main(){
    int g[4] = {2, 0, 1, 0}; // target
    int h[4] = {1,2,3,0};
    struct donations *d = init(4, 4, h);
    // struct donations *d = init(3, 4, g);

    // UNIT TESTING

    printf("initial: \n");
    for (int i = 0; i < d->k; i++){
        printf("{%d: %d} \n", d->curr[i]->k_i, d->curr[i]->s_i);
    }

    assert(!donate(d,1));
    assert(!donate(d,2));
    assert(!donate(d,4));
    assert(!donate(d,1));
    for (int i = 0; i < d->k; i++){
        printf("{%d: %d} \n", d->curr[i]->k_i, d->curr[i]->s_i);
    }


    // donate(d, 2);
    // donate(d, 0);
    // donate(d, 1);
    // donate(d, 2);
    // donate(d, 2);
    // donate(d, 0);
}




