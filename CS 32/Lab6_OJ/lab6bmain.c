#include "expr_parse.h"
#include <stdlib.h>

// PROTOTYPES 

expr_node *_val(uint64_t val);
expr_node *_var(char var);
expr_node *_op(op_type otype, expr_node *l, expr_node *r);
expr_node *_add(expr_node *l, expr_node *r);
expr_node *_sub(expr_node *l, expr_node *r);
expr_node *_mul(expr_node *l, expr_node *r);
int isDigit(char c);
void formatVal(const char *s, expr_node** exprRef, size_t* indexRef);
void formatVar(const char *s, expr_node** exprRef, size_t* indexRef);
void formatOp(const char *s, expr_node** exprRef, size_t* indexRef);
expr_node *parse_expression(const char *s);
void printExpression(expr_node *expr);
void free_expression(expr_node *expr);

// CONSTRUCTORS

expr_node *_val(uint64_t val) {
    expr_node *node = (expr_node*)malloc(sizeof(expr_node));
    node->ntype = VAL;
    node->val = val;
    return node;
}

expr_node *_var(char var) {
    expr_node *node = (expr_node*)malloc(sizeof(expr_node));
    node->ntype = VAR;
    node->var = var;
    return node;
}

expr_node *_op(op_type otype, expr_node *l, expr_node *r) {
    expr_node *node = (expr_node*)malloc(sizeof(expr_node));
    node->ntype = OP;
    node->otype = otype;
    node->left = l;
    node->right = r;
    return node;
}

expr_node *_add(expr_node *l, expr_node *r) { return _op(ADD, l, r); }
expr_node *_sub(expr_node *l, expr_node *r) { return _op(SUB, l, r); }
expr_node *_mul(expr_node *l, expr_node *r) { return _op(MUL, l, r); }

// AUXILIARY FUNCTIONS

int isDigit(char c) {
    return (c >= '0' && c <= '9');
}

void formatVar(const char *s, expr_node** exprRef, size_t* indexRef) {
    *exprRef = _var(*(s + *indexRef));
    (*indexRef)++;
}

void formatVal(const char *s, expr_node** exprRef, size_t* indexRef) {
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
