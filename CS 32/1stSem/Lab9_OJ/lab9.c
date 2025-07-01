#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "downward_path.h"
#include <assert.h>
#define k 200000

// PATH ARRRRRRR

typedef struct PATH{
    int ith;
    int jth;
} PATH;

void visit(int i, int j) {
    printf("(%d, %d)\n", i, j);
}

bool dfs(int i, int j, int r, int c, uint64_t **h, int **visits, int **directions, PATH *paths, int *idx) {
    if (i == r - 1 && j == c - 1) {
        paths[*idx].ith = i;
        paths[*idx].jth = j;
        (*idx)++;
        visits[i][j] = 1;
        return true;
    }

    visits[i][j] = 1;

    for (int x = 0; x < 4; x++) {
        int di = i + directions[x][0];
        int dj = j + directions[x][1];

        if (di >= 0 && di < r && dj >= 0 && dj < c && !visits[di][dj] && h[i][j] >= h[di][dj]) {
            if (dfs(di, dj, r, c, h, visits, directions, paths, idx)) {
                paths[*idx].ith = i;
                paths[*idx].jth = j;
                (*idx)++;
                return true;
            }
        }
    }
    
    return false;
}

bool find_downward_path(int r, int c, uint64_t **h) {
    // cardinal directions
    int **directions = malloc(4 * sizeof(int *));
    for (int i = 0; i < 4; i++) {
        directions[i] = malloc(2 * sizeof(int));
    }

    directions[0][0] = 0;  
    directions[0][1] = 1;  // Right
    directions[1][0] = 0;  
    directions[1][1] = -1; // Left
    directions[2][0] = 1;  
    directions[2][1] = 0;  // Down
    directions[3][0] = -1; 
    directions[3][1] = 0;  // Up


    int **visits = malloc(r * sizeof(int *));
    for (int i = 0; i < r; i++) {
        visits[i] = malloc(c * sizeof(int));
        for (int j = 0; j < c; j++) {
            visits[i][j] = 0;
        }
    }

    
    PATH *paths = malloc(k * sizeof(PATH));
    int idx = 0;
    bool result = dfs(0, 0, r, c, h, visits, directions, paths, &idx);

    if (result) {
        for (int i = idx - 1; i >= 0; i--) {  
            visit(paths[i].ith, paths[i].jth);
        }
    return result;
    }
}

int main() {
    // ----------------------- UNIT_TESTING -----------------------------//


    // TEST #1: 3x3
    int m = 3, n = 3;
    uint64_t **heights = malloc(n * sizeof(uint64_t *));
    for (int i = 0; i < n; i++) {
        heights[i] = malloc(m * sizeof(uint64_t));
    }

    uint64_t row1[] = {5, 0, 0};
    uint64_t row2[] = {0, 0, 0};
    uint64_t row3[] = {0, 0, 0};

    for (int j = 0; j < m; j++) {
        heights[0][j] = row1[j];
        heights[1][j] = row2[j];
        heights[2][j] = row3[j];
    }

    printf("3by3\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%lu ", heights[i][j]);
        }
        printf("\n");
    }

    bool ret = find_downward_path(m, n, heights);
    assert(ret == true );

    // TEST #2: 4x4
    m = 4, n = 4;
    heights = malloc(n * sizeof(uint64_t *));
    for (int i = 0; i < n; i++) {
        heights[i] = malloc(m * sizeof(uint64_t));
    }

    uint64_t row4[] = {5, 1, 1, 0};
    uint64_t row5[] = {6, 6, 6, 0};
    uint64_t row6[] = {1, 0, 1, 0};
    uint64_t row7[] = {1, 0, 0, 0};

    for (int j = 0; j < m; j++) {
        heights[0][j] = row4[j];
        heights[1][j] = row5[j];
        heights[2][j] = row6[j];
        heights[3][j] = row7[j];
    }

    printf("4by4\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%lu ", heights[i][j]);
        }
        printf("\n");
    }

    ret = find_downward_path(m, n, heights);
    assert(ret == true);
}
