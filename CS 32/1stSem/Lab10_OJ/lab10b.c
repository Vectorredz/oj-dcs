#include <stdio.h>
#include <stdlib.h>
#include "path2.h"

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
    int64_t currDiagonal = (dr - 1 >= 0) &&  (dc + 1 < c) ? helper(r, c, m, dr - 1, dc + 1, memo) : -1;

    int64_t minRubble = 0;
    if (currRight < currUp && currRight < currDiagonal){
        minRubble = currRight;
    }
    else if (currUp < currRight && currUp < currDiagonal){
        minRubble = currUp;
    }
    else {
        minRubble = currDiagonal;
    }

    if (minRubble == -1) {
        memo[dr][dc] = -1; // destroyed 
    } else {
        memo[dr][dc] = m[dr][dc] + minRubble;
    }

    return memo[dr][dc];
}

int main() {
    int r = 4, c = 4;

    // Allocate memory for the grid
    int64_t **m = malloc(r * sizeof(int64_t *));
    for (int i = 0; i < r; i++) {
        m[i] = malloc(c * sizeof(int64_t));
    }

    // Initialize the grid
    int64_t grid[4][4] = {
    { 1,  1,  1,  0},
    { 1, -1,  1,  1},
    { 1,  1, -1,  1},
    { 0,  1,  1,  0},};

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            m[i][j] = grid[i][j];
        }
    }

    // Compute and print the result
    int64_t result = poutine_path(4, 4, m);

    printf("minimum rubles Vladimir can earn: %ld\n", result);

    // Free allocated memory
    for (int i = 0; i < r; i++) {
        free(m[i]);
    }
    free(m);

    return 0;
}
