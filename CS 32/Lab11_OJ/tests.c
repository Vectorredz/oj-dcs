#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include "sensousness.h"
#include <stdio.h>

#define MAX_LEN 5001

// Memoization array to store computed sensuousness values
int memo[MAX_LEN][MAX_LEN];

// Function to compute minimum operations to make a substring a palindrome
int compute_sensuousness(const char* s, int start, int end) {
    // Base cases
    if (start >= end) return 0;
    
    // Check if already computed
    if (memo[start][end] != -1) return memo[start][end];
    
    // If first and last characters match, reduce problem size
    if (s[start] == s[end]) {
        memo[start][end] = compute_sensuousness(s, start + 1, end - 1);
        return memo[start][end];
    }
    
    // Try removing first or last character
    int remove_first = 1 + compute_sensuousness(s, start + 1, end);
    int remove_last = 1 + compute_sensuousness(s, start, end - 1);
    
    // Store and return minimum
    memo[start][end] = (remove_first < remove_last) ? remove_first : remove_last;
    return memo[start][end];
}

int64_t sensuousness_sum(const char *s) {
    int n = strlen(s);
    int64_t total_sensuousness = 0;
    
    // Reset memoization array
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            memo[i][j] = -1;
        }
    }
    
    // Compute sensuousness for every substring
    for (int start = 0; start < n; start++) {
        for (int end = start; end < n; end++) {
            total_sensuousness += compute_sensuousness(s, start, end);
        }
    }
    
    return total_sensuousness;
}

int main(){
    int64_t ret = sensuousness_sum("philip");
    printf("%lu ", ret);

    int64_t ret1 = sensuousness_sum("z");
    printf("%lu ", ret1);

    int64_t ret2 = sensuousness_sum("zZ");
    printf("%lu ", ret2);

}