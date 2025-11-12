#include <stdlib.h>
#include "lunchly.h"

void is_prime(int n, int *primes) {
    for (int i = 2; i * i < n; i++) {
        if (primes[i] == 1) {
            for (int d = i * i; d < n; d += i) {
                primes[d] = 0;
            }
        }
    }
}

int enumerate_lunchly_numbers(int m, int *out){
    if (m < 2) {return 0;}
    int *p = malloc((m + 1) * sizeof(int));
    if (!p) {return 0;}
    for (int i = 0; i <= m; ++i) {
         p[i] = 1;  p[0] = p[1] = 0;
    }
    for (int i = 2; (long long)i * i <= m; ++i) {
        if (p[i]) { 
            for (int d = i * i; d <= m; d += i){ 
                p[d] = 0; 
            }
        } 
    }
    int count = 0;
    for (int i = 2; i <= m; ++i) {
        int pr = 0, np = 0;
        for (int d = 10; d <= i * 10; d *= 10) {
            int x = i % d;       
            if (p[x]) {
                ++pr;
            }
            else {
                ++np;
            }
            if (d > (int)1e8) {
                break; 
            }
        }
        if (pr > np) {
            out[count++] = i;
        } 
    }
    free(p);
    return count;
}
