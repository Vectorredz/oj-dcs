#ifndef _TABULATE_H
#define _TABULATE_H

typedef long long int int64;

void tabulate(int r, int c, char **headers, int64 **data);
void tabulate_sep(int r, int c, char **headers, int64 **data, char sep);

#endif
