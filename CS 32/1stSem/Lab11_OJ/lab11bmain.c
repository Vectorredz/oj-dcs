#include <stdlib.h>
#include "shirts.h"

void bubble_sort(int64_t *p, int n);
int64_t *copy_arr(int n, int64_t *p);

void bubble_sort(int64_t *p, int n) {

    for (int i = 0; i < n - 1; i++) { 

        int flag_swap = 0; 

        for (int j = 0; j < n - i - 1; j++) {
            if (p[j] > p[j + 1]) {
                // Swap
                int64_t temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
                flag_swap = 1; 
            }
        }
        if (!flag_swap){
            break;
        }
    }
}

// create copy arr

int64_t *copy_arr(int n, int64_t *p){
    int64_t *clone = malloc(n * sizeof(int64_t));

    for (int i = 0; i < n; i++){
        clone[i] = p[i];
    }
    return clone;
}


int64_t cheapest_shirts(int n, int64_t *p){

    // sort the clone
    int64_t *clone = copy_arr(n, p);

    bubble_sort(clone, n);

    // partition in 3 

    if (n == 0){
        return 0;
    }

    int k = (n / 3) * 2;

    int64_t sum = 0;

    for (int i = 1; i < k; i += 2){
        sum += clone[i] * 3;
    }

    return sum;
}