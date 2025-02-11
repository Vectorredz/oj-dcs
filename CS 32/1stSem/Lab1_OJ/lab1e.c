#include <stdio.h>
#include "baggage5.h"
#include <stdlib.h>

// sum of dims <= b -> allow
// return number of suitable bags
// return via pointer the suitable bags
int suitable_suitcases(long long int b, suitcase_t *s, int n, int **res){
    unsigned long long int sum = 0;
    int *bags =(int*)malloc(sizeof(long long int)*n);
    int count = 0;
    int j = 0;
    for (size_t i = 0; i < n; i++){
        sum = s[i].l + s[i].w + s[i].h;
        if (sum <= b){
            bags[j++] = i+1;
            count++;
        }
    }
    *res = bags;
    return count;
}

int main() {
    suitcase_t suitcases[6] = {
        {3, 1, 4},
        {1, 5, 9},
        {2, 6, 5},
        {3, 5, 8},
        {9, 7, 9},
        {3, 2, 3},
    };
    
    int *res;
    int ret = suitable_suitcases(13, suitcases, 6, &res);
    // for (int i = 0; i < ret; i++){
    //     printf("%d ", res[i]);
    // }
    free(res);

    return 0;
}