#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
void split_digits(int num, int *n, char *digits, char **arrOfDigits) {
    sprintf(digits, "%d", num);  
    int len = strlen(digits);
    *n = len;

    // build partial digit strings
    for (int i = 0; i < len; i++) {
        arrOfDigits[i] = malloc(20 * sizeof(char));
        strncpy(arrOfDigits[i], digits + i, len - i);
        arrOfDigits[i][len - i] = '\0';
    }
}

int is_lunchy(int n, char **arrOfDigits, int digit, int *primes) {
    int prime = 0, nonprime = 0;

    for (int i = 0; i < n; i++) {
        int num;
        sscanf(arrOfDigits[i], "%d", &num);
        if (num < 0) continue;
        if (primes[num]) prime++;
        else nonprime++;
    }

    return (prime > nonprime) && primes[digit];
}

int enumerate_lunchly_numbers(int m, int *out) {
    int *primes = malloc(m * sizeof(int));
    int len = 0;

    for (int i = 0; i < m; i++) primes[i] = 1;
    primes[0] = primes[1] = 0;

    is_prime(m, primes); // preprocess prime numbers from 2 to m
    int j = 0; 
    for (int i = 2; i < m; i++) {
        char **arrOfDigits = malloc(20 * sizeof(char *));
        char *digits = malloc(20 * sizeof(char)); 
        split_digits(i, &len, digits, arrOfDigits);
        int ret = is_lunchy(len, arrOfDigits, i, primes);
        if (ret == 1) {
            printf("%d \n", i);
            out[j+=1] = i;
        }
    }
    return j;
}
int main() {
    int out[30];
    int ret = enumerate_lunchly_numbers(30, out);
    return 0;
}
