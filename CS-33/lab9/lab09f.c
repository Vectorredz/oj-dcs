#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "giveaway.h"

int64_t *_extended_gcd(int64_t a, int64_t b, int64_t *tuple) {
    if (b == 0) {
        tuple[0] = a;
        tuple[1] = 1;
        tuple[2] = 0;
        return tuple;
    }

    int64_t temp[3];
    _extended_gcd(b, a % b, temp);

    int64_t g  = temp[0];
    int64_t x1 = temp[1];
    int64_t y1 = temp[2];

    tuple[0] = g;
    tuple[1] = y1;
    tuple[2] = x1 - (a / b) * y1;

    return tuple;
}

int64_t *extended_gcd(int64_t a, int64_t b) {
    int64_t *tuple = malloc(3 * sizeof(int64_t));
    return _extended_gcd(a, b, tuple);
}

int64_t min_choc_packs(int64_t b, int64_t p) {
    int64_t *tuple = extended_gcd(b, p);
    int64_t g = tuple[0], x = tuple[1];
    if (g != 1) {return -1;}
    int64_t inv = (x % p + p) % p;
    int64_t n = (-inv % p + p) % p;
    if (n == 0) {n = p;}
    return n;
}

int main() {
    printf("%ld\n", min_choc_packs(6, 7));  // → 1
    printf("%ld\n", min_choc_packs(4, 2));  // → -1
    printf("%ld\n", min_choc_packs(5, 9));  // → 7
}
