#ifndef PATHS_H
#define PATHS_H

typedef struct road {
    int city1;
    int city2;
} road;

void visit(int city);

void find_path(int n, int e, road *roads);

#endif
