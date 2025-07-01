#include <stdio.h>
#include <stdlib.h>
#include "shirts.h"
#include <assert.h>

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

    int j = 0; 
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

    int j = 0;
    int flag = 0;
    int k = (n / 3) * 2;

    int64_t sum = 0;

    for (int i = 1; i < k; i += 2){
        sum += clone[i] * 3;
    }

    return sum;
}


int main() {
    int n = 12;
    int64_t arr[] = {1,2,3,4,5,6,7,8,9,10,11,12};
    int64_t ret = cheapest_shirts(n, arr);

    // test_case # 1

    int n1 = 3; 
    int64_t arr1[] = {1,4,9};
    int64_t ret1 = cheapest_shirts(n1, arr1);
    assert(ret1 == 12);

    // test_case # 2
    
    int n2 = 3; 
    int64_t arr2[] = {4,1,9};
    int64_t ret2 = cheapest_shirts(n2, arr2);

     // test_case # 1

    int n3 = 6; 
    int64_t arr3[] = {1,2,3,4,5,6};
    int64_t ret3 = cheapest_shirts(n3, arr3);
    assert(ret3 == 18);

    // test_case # 2
    
    int n4 = 9; 
    int64_t arr4[] = {1,2,3,4,5,6,7,8,9};
    int64_t ret4 = cheapest_shirts(n4, arr4);
    assert(ret4 == 36);

    int n5 = 0; 
    int64_t arr5[] = {};
    int64_t ret5 = cheapest_shirts(n5, arr5);
    assert(ret5 == 0);


}