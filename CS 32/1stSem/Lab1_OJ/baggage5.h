#ifndef _BAGGAGE5_H
#define _BAGGAGE5_H

typedef long long int int64;

typedef struct suitcase {
    int l;
    int w;
    int h;
} suitcase_t;

int suitable_suitcases(int64 b, suitcase_t *s, int n, int **res);

#endif