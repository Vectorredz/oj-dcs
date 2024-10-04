#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef long long int int64;

int64 eye_count(int64 *s, int n) {
    if (n < 3) return 0;

    int64 count = 0;

    // Arrays to store prefix and suffix counts
    int64 *prefix_less = (int64 *)calloc(n, sizeof(int64));
    int64 *suffix_less = (int64 *)calloc(n, sizeof(int64));
    
    if (prefix_less == NULL || suffix_less == NULL) {
        perror("Failed to allocate memory");
        exit(EXIT_FAILURE);
    }

    // Calculate prefix counts
    for (int j = 1; j < n; ++j) {
        for (int i = 0; i < j; ++i) {
            if (s[i] < s[j]) {
                prefix_less[j]++;
            }
        }
    }

    // Calculate suffix counts
    for (int j = 0; j < n - 1; ++j) {
        for (int k = j + 1; k < n; ++k) {
            if (s[k] < s[j]) {
                suffix_less[j]++;
            }
        }
    }

    // Calculate the number of valid triples
    for (int j = 1; j < n - 1; ++j) {
        count += prefix_less[j] * suffix_less[j];
    }

    free(prefix_less);
    free(suffix_less);

    return count;
}

int main() {
    int64 s[] = {2, 7, 1, 8, 2, 8, 1, 8, 2};
    int64 ret = eye_count(s, 9);
    assert(ret == 11);
    printf("The number of eye subsequences is: %lld\n", ret);
    return 0;
}
