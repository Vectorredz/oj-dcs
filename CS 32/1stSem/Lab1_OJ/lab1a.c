#include <stdio.h>
#include "baggage.h"
#include <stdbool.h>
#include <assert.h>
#include <math.h>

bool within_limit(int l, int w, int h, long long int b){
    if ((double long)l  * (double long)w * (double long)h < (double long)b){
        return true;
    }
    else {
        return false;
    }
}

int main(){
    assert (within_limit(2,3,4,5) == false);
    assert (within_limit(2, 3, 4, 24) == false);
    assert (within_limit(2, 3, 4, 25)== true);

    assert(within_limit(1, 1, 1, 1) == false);
    assert(within_limit(1, 1, 1, 2) == true);
    assert(within_limit(pow(10, 9), pow(10, 9), pow(10, 9), pow(10, 18)) == false);
    assert(within_limit(pow(10, 9), pow(10, 9), pow(10, 9), pow(10, 18) + 1) == false);

    return 0;
}