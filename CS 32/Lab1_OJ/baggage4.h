#ifndef _BAGGAGE4_H
#define _BAGGAGE4_H

typedef long long int int64;

typedef struct suitcase {
    int l;
    int w;
    int h;
} suitcase_t;

int64 max_vol_suitcase(int64 b, suitcase_t *s, int n);

#endif
