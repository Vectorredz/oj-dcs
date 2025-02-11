#include <stdio.h>
#include <stdlib.h>

long unsigned int excitement(unsigned int s1, unsigned int s2, long unsigned int total) {
    long unsigned int ret = 0;
    if (total % 2 == 0) {
        ret += total + s1 + s2 + 1;
    } else {
        ret += total;
    }
    return ret;
}

long unsigned int combinatorics(long unsigned int *skills, long unsigned int n) {
    long unsigned int results[1000];
    long unsigned int final = 0;
    unsigned int z = 0;
    for (unsigned int u = 0; u < n; u++) {
        for (unsigned int v = u + 1; v < n; v++) {  // Start v from u + 1 to avoid duplicate pairs
            long unsigned int ret = skills[u] * skills[v];
            results[z] = ret;
            final += excitement(skills[u], skills[v], ret);
            z++;
        }
    }
    printf("%lu\n", final);
    return final;  // Return the final result
}

int main() {
    unsigned int t;
    scanf("%u", &t);

    for (unsigned int i = 0; i < t; i++) {
        long unsigned int n;
        scanf("%lu", &n);

        long unsigned int *skills = (long unsigned int *)malloc(n * sizeof(long unsigned int));
        if (skills == NULL) {
            printf("Memory allocation failed\n");
            return 1;
        }

        for (unsigned int j = 0; j < n; j++) {
            scanf("%lu", &skills[j]);
        }

        combinatorics(skills, n);
        free(skills);
    }

    return 0;
}
