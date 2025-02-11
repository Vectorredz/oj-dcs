#include "expr_parse.h"

#include <stdbool.h>
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

#define VERIFY(b) do {\
    fprintf(stderr, "verifying: %s\n", (#b));\
    bool _b = (b);\
    if (!_b) {\
        fprintf(stderr, "verification failed!\n");\
        exit(1);\
    }\
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

// PROTOTYPES 

expr_node *_val(uint64_t val);
expr_node *_var(char var);
expr_node *_op(char otype, expr_node *l, expr_node *r);
expr_node *_add(expr_node *l, expr_node *r);
expr_node *_sub(expr_node *l, expr_node *r);
expr_node *_mul(expr_node *l, expr_node *r);
int isDigit(char c);
void formatVal(const char *s, expr_node** exprRef, size_t* indexRef);
void formatVar(const char *s, expr_node** exprRef, size_t* indexRef);
void formatOp(const char *s, expr_node** exprRef, size_t* indexRef);
expr_node *parse_expression(const char *s);
void printExpression(expr_node *expr);
bool expressions_equal(expr_node *a, expr_node *b);
void free_expression(expr_node *expr);

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

void formatVar(const char *s, expr_node **exprRef, size_t *indexRef) {
    *exprRef = _var(*(s + *indexRef));
    (*indexRef)++;
}

void formatVal(const char *s, expr_node **exprRef, size_t *indexRef) {
    size_t endIndex = *indexRef;
    while (isDigit(*(s + endIndex))) {
        endIndex++;
    }

    char* valueStr = (char*)malloc((endIndex - *indexRef + 1) * sizeof(char));  
    size_t count = 0;
    for (size_t k = *indexRef; k < endIndex; k++) {
        valueStr[count++] = s[k];
    }
    valueStr[count] = '\0';

    *indexRef = endIndex;
    *exprRef = _val(atoll(valueStr));
    free(valueStr);
}

void formatOp(const char *s, expr_node** exprRef, size_t* indexRef) {
    expr_node* leftExpr = NULL;
    char operatorType = 0;
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
    // skips the space and jumps directly to the next ntype
    currentIndex++;
    currentChar = *(s + currentIndex);
    operatorType = currentChar;
    currentIndex += 2;
    currentChar = *(s + currentIndex);

    if (currentChar == ')') {
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

void free_expression(expr_node *expr) {
    if (expr == NULL) return;
    free_expression(expr->left);
    free_expression(expr->right);
    free(expr);
}


int main() {
    expr_node *x = _var('x');
    expr_node *parsed_expr = parse_expression("(x + 143) * (x - 143)");
    expr_node *expected_expr = _mul(_add(x, _val(143)), _sub(x, _val(143)));

    VERIFY(expressions_equal(parsed_expr, expected_expr));

    printf("All tests passed!\n");

    // Free allocated memory
    free_expression(parsed_expr);
    free_expression(expected_expr);
    free_expression(x);

    return 0;
}
