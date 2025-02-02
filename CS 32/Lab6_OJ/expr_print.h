#ifndef EXPR_PRINT_H
#define EXPR_PRINT_H

#include <stdint.h>

typedef enum node_type_enum { VAL, VAR, OP } node_type;
typedef enum op_type_enum { ADD, SUB, MUL } op_type;

// a tagged union
typedef struct expr_node {
    node_type ntype;
    union {
        uint64_t val;
        char var;
        struct {
            op_type otype;
            struct expr_node *left;
            struct expr_node *right;
        };
    };
} expr_node;

void print_expression(expr_node *expr);

#endif
