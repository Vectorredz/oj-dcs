#ifndef SAVINGS_H
#define SAVINGS_H

#include <stdint.h>

typedef struct wire {
    int a, b;
    int64_t c;
} wire;

int64_t maximum_savings(int n, int w, int r, wire *wires);

#endif