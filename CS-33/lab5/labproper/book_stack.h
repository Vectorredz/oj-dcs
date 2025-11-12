#ifndef BOOK_STACK_H
#define BOOK_STACK_H

#include <stdint.h>

typedef struct t_stack t_stack;

t_stack *t_init(void);
void t_push(t_stack *ts, const char *t, int64_t q);
char *t_pop(t_stack *ts);
char *t_peek(t_stack *ts);
void t_top_three(t_stack *ts, char *res1, char *res2, char *res3);
void time_travel(t_stack *ts, int k);
#endif