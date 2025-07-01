#ifndef PATH3_H
#define PATH3_H

#include <stdint.h>

typedef enum cell_type { NORMAL, FRIENDLY, DANGEROUS } cell_type;

int64_t poutine_path(int r, int c, cell_type **grid);

#endif
