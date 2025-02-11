#include "expr_parse.h"
#include <stdbool.h>
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

bool expressionsEqual(expr_node *a, expr_node *b);

#define VERIFY(b) do { \
    fprintf(stderr, "verifying: %s\n", (#b)); \
    bool _b = (b); \
    if (!_b) { \
        fprintf(stderr, "verification failed!\n"); \
        exit(1); \
    } \
} while (0)

bool expressions_equal(expr_node *a, expr_node *b) {
    if (a->ntype != b->ntype) {
        return false;
    } else if (a->ntype == VAL) {
        return a->val == b->val;
    } else if (a->ntype == VAR) {
        return a->var == b->var;
    } else {
        assert(a->ntype == OP);
        return (
            a->otype == b->otype
            && expressions_equal(a->left, b->left)
            && expressions_equal(a->right, b->right)
        );
    }
}

// CONSTRUCTORS

expr_node *_val(uint64_t val) {
    expr_node *node = (expr_node*)malloc(sizeof(expr_node));
    node->ntype = VAL;
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

expr_node *_var(char var) {
    expr_node *node = (expr_node*)malloc(sizeof(expr_node));
    node->ntype = VAR;
    node->var = var;
    node->left = NULL;
    node->right = NULL;
    return node;
}

expr_node *_op(char otype, expr_node *l, expr_node *r) {
    expr_node *node = (expr_node*)malloc(sizeof(expr_node));
    node->ntype = OP;
    node->otype = otype;
    node->left = l;
    node->right = r;
    return node;
}

expr_node *_add(expr_node *l, expr_node *r) { return _op('+', l, r); }
expr_node *_sub(expr_node *l, expr_node *r) { return _op('-', l, r); }
expr_node *_mul(expr_node *l, expr_node *r) { return _op('*', l, r); }

// AUXILIARY FUNCTIONS

int isDigit(char c) {
    return (c >= '0' && c <= '9');
}

void formatVal(const char *s, expr_node** exprRef, size_t* indexRef) {
    size_t j = 0;
    size_t endIndex = *indexRef;
    while (isDigit(*(s + endIndex))) {
        endIndex++;
    }

    char* valueStr = (char*)malloc(j * sizeof(char));  
    size_t count = 0;
    for (size_t k = *indexRef; k < endIndex; k++) {
        *(valueStr + count) = *(s + k);
        count++;
    }

    *indexRef = endIndex;
    *exprRef = _val(atoll(valueStr));
}

void formatVar(const char *s, expr_node** exprRef, size_t* indexRef) {
    *exprRef = _var(*(s + *indexRef));
    *indexRef = *indexRef + 1;
}

void formatOp(const char *s, expr_node** exprRef, size_t* indexRef) {
    expr_node* leftExpr = NULL;
    op_type operatorType = ADD;
    expr_node* rightExpr = NULL;

    size_t currentIndex = *indexRef + 1;
    char currentChar = *(s + currentIndex);
    if (currentChar == '(') {
        formatOp(s, &leftExpr, &currentIndex);
    } else if (isDigit(currentChar)) {
        formatVal(s, &leftExpr, &currentIndex);
    } else {
        formatVar(s, &leftExpr, &currentIndex);
    }
    currentChar = *(s + currentIndex);
    if (currentChar == '\0') {
        *exprRef = leftExpr;
        return;
    }

    currentIndex++;
    currentChar = *(s + currentIndex);
    operatorType = currentChar;
    currentIndex += 2;
    currentChar = *(s + currentIndex);

    if (currentChar == '(') {
        formatOp(s, &rightExpr, &currentIndex);
    } else if (isDigit(currentChar)) {
        formatVal(s, &rightExpr, &currentIndex);
    } else {
        formatVar(s, &rightExpr, &currentIndex);
    }

    currentIndex++;
    *indexRef = currentIndex;

    if (operatorType == '+') {
        (*exprRef) = _add(leftExpr, rightExpr);
    } else if (operatorType == '-') {
        (*exprRef) = _sub(leftExpr, rightExpr);
    } else if (operatorType == '*') {
        (*exprRef) = _mul(leftExpr, rightExpr);
    }
}

expr_node *parse_expression(const char *s) {
    expr_node* exp = NULL;
    size_t index = -1;  
    formatOp(s, &exp, &index);
    return exp;
}

int main() {
    expr_node *x = _var('x');
    expr_node *one = _val(1);
    expr_node *three = _add(_add(one, one), one);   
    VERIFY(expressions_equal(parse_expression("(1 - 1) * (((1 + 1) + 1) * ((1 + 1) + 1))"),
    _mul(
            _sub(one, one),
            _mul(three, three)
        )
    ));

    printf("test passed!\n");
}
