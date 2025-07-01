#ifndef STROLL_H
#define STROLL_H

typedef struct road {
    int start;
    int end;
} road;

void visit(int i);

void find_leisurely_path(int n, int r, road *roads);

#endif
