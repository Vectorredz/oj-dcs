#include <stdio.h>
#include "baggage3.h"
#include <assert.h>

suitcase_t better_suitcase(suitcase_t s1, suitcase_t s2) {
    unsigned long long int vol1 = (unsigned long long int)s1.l * (unsigned long long int)s1.w * (unsigned long long int)s1.h;
    unsigned long long int vol2 = (unsigned long long int)s2.l * (unsigned long long int)s2.w * (unsigned long long int)s2.h;
    if (vol1 > vol2) {
        return s1;
    } else if (vol1 < vol2) {
        return s2;
    } else {
        return s1;
    }
}

int main() {
    suitcase_t s1 = {{3,1,4}, {2,2,4}};
    suitcase_t s2 = {2,2,4};
    // suitcase_t result = better_suitcase(s1, s2);
    printf("%d", s1.l);
    printf("%d", s2.l);

    
    return 0;
}
