#include "savings.h"
#include <stdint.h>
#include <stdlib.h>

// UNION-FIND algowwww ----------------------------------------------

int find(int x, int *uf) {
    if (uf[x] != x) {
        uf[x] = find(uf[x], uf);
    }
    return uf[x];
}

void unionSet(int x, int y, int *uf) {
    int rx = find(x, uf);
    int ry = find(y, uf);
    uf[rx] = ry;
}
// -------------------------------------------------------------------

int infinitelyLongWiresComparison(const void *a, const void *b) {
    wire *wa = (wire *)a;
    wire *wb = (wire *)b;
    if (wb->c == wa->c){
        return 0;
    }
    if (wb->c > wa->c){
        return -1; // return -1, imposibleng task
    }
    else {
        return 1;
    }
}

int64_t maximum_savings(int n, int w, int r, wire *wires) {
 
    qsort(wires, w, sizeof(wire), infinitelyLongWiresComparison);

    int *uf = (int *)calloc(n, sizeof(int));
    if (uf == NULL) {
        return -1; 
    }

    for (int i = 0; i < n; i++){
        uf[i] = i;
    }

    int64_t savings = 0;
    int removed = 0;
    for (int i = 0; i < w; i++) {
        int a = wires[i].a, b = wires[i].b;
        if (find(a, uf) != find(b, uf)) { 
            unionSet(a, b, uf);
        } else if (removed < r) { 
            savings += wires[i].c;
            removed++;
        }
    }
    if (removed < r){
        return -1;
    }
    return savings;
}
