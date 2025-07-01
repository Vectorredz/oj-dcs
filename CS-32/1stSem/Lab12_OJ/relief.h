#ifndef RELIEF_H
#define RELIEF_H

#include <stdbool.h>

struct donations;

struct donations *init(int k, int r, const int *b);

bool donate(struct donations *d, int d_i);

#endif
