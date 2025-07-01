#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tabulate.h"
#include <assert.h>

void tabulate(int r, int c, char **headers, long long int **data) {
    
    int lens[c];
    int j = 0;
    for (int i = 0; i < c; i++) {
        lens[j++] = strlen(headers[i])+1;
        if (i == c-1){
            printf("| %*s |", lens[i], headers[i]);
        }
        else {
            printf("| %*s ", lens[i], headers[i]);
        }
    }
    printf("\n");

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (j == c-1){
                printf("| %*lld |", lens[j], data[i][j]);
            }
            else {
                printf("| %*lld ", lens[j], data[i][j]);

            }
        }
        printf("\n");
    }
}

void tabulate_sep(int r, int c, char **headers, long long int **data, char sep){
    int lens[c];
    int j = 0;
    for (int i = 0; i < c; i++) {
        lens[j++] = strlen(headers[i])+1;
        if (i == c-1){
            printf("%c %*s %c", sep, lens[i], headers[i], sep);
        }
        else {
            printf("%c %*s ", sep, lens[i], headers[i]);
        }
    }
    printf("\n");

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (j == c-1){
                printf("%c %*lld %c", sep, lens[j], data[i][j], sep);
            }
            else {
                printf("%c %*lld ", sep, lens[j], data[i][j]);

            }
        }
        printf("\n");
    }
}



int main() {
    char *headers[] = {"n", "fib(n)", "factorial(n)"};
    int r = 16, c = 3;

    long long int **data = (long long int **)malloc(r * sizeof(long long int *));
    for (int i = 0; i < r; i++) {
        data[i] = (long long int *)malloc(c * sizeof(long long int));
    }

    long long int init_data[16][3] = {
    {0, 0, 1},
    {1, 1, 1},
    {2, 1, 2},
    {3, 2, 6},
    {4, 3, 24},
    {5, 5, 120},
    {6, 8, 720},
    {7, 13, 5040},
    {8, 21, 40320},
    {9, 34, 362880},
    {10, 55, 3628800},
    {11, 89, 39916800},
    {12, 144, 479001600},
    {13, 233, 6227020800LL},
    {14, 377, 87178291200LL},
    {15, 610, 1307674368000LL},
};

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            data[i][j] = init_data[i][j];
        }
    }

    char sep = '*';
    tabulate_sep(r, c, headers, data, sep);

    for (int i = 0; i < r; i++) {
        free(data[i]);
    }
    free(data);

    return 0;
}
