#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "path3.h"

#define MOD 1000000000


int64_t poutine_path(int r, int c, cell_type **grid) {
    int max_hp = r + c;  // Maximum HP Vladimir can gain/lose
    int64_t ***dp = malloc(2 * sizeof(int64_t **));  // Rolling DP layers
    
    for (int k = 0; k < 2; ++k) {
        dp[k] = malloc(c * sizeof(int64_t *));
        for (int j = 0; j < c; ++j) {
            dp[k][j] = calloc(max_hp + 1, sizeof(int64_t));
        }
    }

    // Initial condition: Vladimir starts at (r-1, 0) with 1 HP
    dp[(r - 1) % 2][0][1] = 1;

    // Bottom-up DP
    for (int i = r - 1; i >= 0; --i) {
        for (int j = 0; j < c; ++j) {
            for (int hp = 0; hp <= max_hp; ++hp) {
                if (dp[i % 2][j][hp] == 0) continue;

                // Determine HP adjustment for current cell
                int new_hp = hp;
                if (grid[i][j] == FRIENDLY) new_hp += 1;
                else if (grid[i][j] == DANGEROUS) new_hp -= 1;

                if (new_hp <= 0 || new_hp > max_hp) continue;

                // Transition to (i-1, j)
                if (i - 1 >= 0) {
                    dp[(i - 1) % 2][j][new_hp] = 
                        (dp[(i - 1) % 2][j][new_hp] + dp[i % 2][j][hp]) % MOD;
                }

                // Transition to (i, j+1)
                if (j + 1 < c) {
                    dp[i % 2][j + 1][new_hp] = 
                        (dp[i % 2][j + 1][new_hp] + dp[i % 2][j][hp]) % MOD;
                }

                // Transition to (i-1, j+1)
                if (i - 1 >= 0 && j + 1 < c) {
                    dp[(i - 1) % 2][j + 1][new_hp] = 
                        (dp[(i - 1) % 2][j + 1][new_hp] + dp[i % 2][j][hp]) % MOD;
                }
            }
            // Clear current cell state after processing
            free(dp[i % 2][j]);
            dp[i % 2][j] = calloc(max_hp + 1, sizeof(int64_t));
        }
    }

    // Sum all paths reaching (0, c-1)
    int64_t result = 0;
    for (int hp = 1; hp <= max_hp; ++hp) {
        result = (result + dp[0][c - 1][hp]) % MOD;
    }

    // Free memory
    for (int k = 0; k < 2; ++k) {
        for (int j = 0; j < c; ++j) {
            free(dp[k][j]);
        }
        free(dp[k]);
    }
    free(dp);

    return result;
}
#include <stdio.h>
#include <stdlib.h>
#include "path3.h"

int main() {
    int r = 3, c = 5;

    // Allocate memory for the grid
    cell_type **grid = malloc(r * sizeof(cell_type *));
    for (int i = 0; i < r; i++) {
        grid[i] = malloc(c * sizeof(cell_type));
    }

    // Initialize the grid with sample values
    cell_type initial_grid[3][5] = {
        {NORMAL,   NORMAL,    NORMAL, DANGEROUS, NORMAL},
        {NORMAL, FRIENDLY, DANGEROUS,    NORMAL, NORMAL},
        {NORMAL,   NORMAL,    NORMAL,    NORMAL, NORMAL},
    };

    // Copy the initial values to the allocated grid
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            grid[i][j] = initial_grid[i][j];
        }
    }

    // Compute the number of valid paths
    int64_t result = poutine_path(r, c, grid);
    printf("Number of valid paths: %ld\n", result);

    // Free allocated memory for the grid
    for (int i = 0; i < r; i++) {
        free(grid[i]);
    }
    free(grid);

    return 0;
}
