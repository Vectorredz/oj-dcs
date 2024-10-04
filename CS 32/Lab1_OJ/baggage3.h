#ifndef _BAGGAGE3_H
#define _BAGGAGE3_H
typedef struct suitcase suitcase_t;
struct suitcase {
    int l;
    int w;
    int h;
};

suitcase_t better_suitcase(suitcase_t *s1, suitcase_t s2);

#endif