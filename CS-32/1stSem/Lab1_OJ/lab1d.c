#include <stdio.h>
#include "baggage4.h"
#include <assert.h>

long long int max_vol_suitcase(long long int b, suitcase_t *s, int n){
    unsigned long long int curr = 0;
    unsigned long long int sum = 0;
    unsigned long long int vol = 0;
    for (int i = 0; i < n; i++){
        vol = (unsigned long long int)s[i].l * (unsigned long long int)s[i].w * (unsigned long long int)s[i].h;
        sum = (unsigned long long int)s[i].l + (unsigned long long int)s[i].w + (unsigned long long int)s[i].h;
        if (vol > curr && sum <= b){
            curr = vol;
        }
    }
    return curr;
}

int main(){
    suitcase_t s[] = {{3, 1, 4}, {1, 5, 9}, {2, 6, 5}, {3, 5, 8}, {9, 7, 9}, {3, 2, 3}};
    assert (max_vol_suitcase(13, s, 6) == 60);
    assert (max_vol_suitcase(1, s, 6) == 0);
    return 0;
}