#include <stdlib.h>
#include "downward_path.h"
#define k 200000

// PATH ARRRRRRR

typedef struct PATH{
    int ith;
    int jth;
} PATH;

typedef struct PATH{
    int ith;
    int jth;
} PATH;

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