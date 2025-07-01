#include <stdio.h>
#include <stdlib.h>
#include "path1.h"

int64_t helper(int r, int c, int64_t **m, int dr, int dc, int64_t **memo);

int64_t poutine_path(int r, int c, int64_t **m) {
    int64_t **memo = malloc(r * sizeof(int64_t *));
    for (int i = 0; i < r; i++) {
        memo[i] = malloc(c * sizeof(int64_t));
        for (int j = 0; j < c; j++) {
            memo[i][j] = -1;
        }
    }

    int64_t result = helper(r, c, m, r-1, 0, memo);

    return result;
}

int64_t helper(int r, int c, int64_t **m, int dr, int dc, int64_t **memo) {
    if (dr < 0 || dc >= c || m[dr][dc] == -1) {
        return -1;
    }

    // base case
    if (dr == 0 && dc == c-1) {
        return m[dr][dc];
    }

    if (memo[dr][dc] != -1) {
        return memo[dr][dc];
    }

    int64_t currRight = (dc + 1 < c) ? helper(r, c, m, dr, dc + 1, memo) : -1;
    int64_t currUp = (dr - 1 >= 0) ? helper(r, c, m, dr - 1, dc, memo) : -1;

    int64_t maxRubble = 0;
    if (currRight > currUp){
        maxRubble = currRight;
    }
    else {
        maxRubble = currUp;
    }

    if (maxRubble == -1) {
        memo[dr][dc] = -1; // destroyed 
    } else {
        memo[dr][dc] = m[dr][dc] + maxRubble;
    }

    return memo[dr][dc];
}

int main() {
    int r = 5, c = 6;

    // Allocate memory for the grid
    int64_t **m = malloc(r * sizeof(int64_t *));
    for (int i = 0; i < r; i++) {
        m[i] = malloc(c * sizeof(int64_t));
    }

    // Initialize the grid
    int64_t grid[5][6] = {
    {50,  9, -1,  2,  0,  0},
    { 7,  4,  2,  2,  1,  1},
    { 9,  6, -1, 99,  1, -1},
    { 5,  5,  5, -1,  9, 11},
    { 0,  1,  1,  8, 10,  1},
};
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            m[i][j] = grid[i][j];
        }
    }

    // Compute and print the result
    int64_t result = poutine_path(r, c, m);
    printf("Maximum rubles Vladimir can earn: %ld\n", result);

    // Free allocated memory
    for (int i = 0; i < r; i++) {
        free(m[i]);
    }
    free(m);

    return 0;
}
