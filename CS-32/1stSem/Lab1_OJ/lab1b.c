#include "baggage2.h"
#include <stdio.h>
#include <assert.h>


int bag(int l, int w, int h, int x, int y){
    if ((unsigned long long int)l + (unsigned long long int)w + (unsigned long long int)h <= x){
        return HANDCARRY;
    }
    else if ((unsigned long long int)l + (unsigned long long int)w + (unsigned long long int)h <= y){
        return CHECK_IN;
    }
    else {
        return GARBAGE;
    }
}

int main(){
    assert (bag(3, 1, 4, 11, 22) == HANDCARRY);
    assert (bag(3, 14, 1, 11, 22) == CHECK_IN);
    assert (bag(31, 4, 15, 11, 22) == GARBAGE);

    return 0;
}