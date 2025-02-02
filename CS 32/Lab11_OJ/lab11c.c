#include "savings.h"
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
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


int main() {
    int n = 4; // Number of computers
    int w = 4; // Number of wires
    int r = 1; // Number of wires to remove

    wire wires[] = {
        {0, 1, 30}, // Computer 0 connected to Computer 1 with cost 30
        {1, 2, 10}, // Computer 1 connected to Computer 2 with cost 10
        {2, 3, 30}, // Computer 2 connected to Computer 3 with cost 30
        {3, 0, 20}  // Computer 3 connected to Computer 0 with cost 20
    };

    int64_t max_savings = maximum_savings(n, w, r, wires);

    if (max_savings == -1) {
        printf("Impossible to remove %d wires without disconnecting the network.\n", r);
    } else {
        printf("Maximum savings by removing %d wire(s): %lld\n", r, max_savings);
    }

    return 0;
}