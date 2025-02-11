#ifndef DOWNWARD_PATH_H
#define DOWNWARD_PATH_H

#include <stdbool.h>
#include <stdint.h>

void visit(int i, int j);

bool find_downward_path(int r, int c, uint64_t **h);

#endif
