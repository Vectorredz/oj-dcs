#include "expr_count.h"
#include <stdlib.h>
#define MOD 323

int64_t terms_in_expansion(expr_node *expr){
    if (expr == NULL){
    return 0;
    }
    if (expr->ntype == OP){
        if (expr->otype == MUL){
            if  ((expr->left->ntype == VAR) || (expr->right->ntype == VAR)){
                return 1;
            }
            else {
                return (1 * (terms_in_expansion(expr->left) * terms_in_expansion(expr->right))) % MOD;
            }
        }
        else if (expr->otype == SUB){
            return (terms_in_expansion(expr->left) + terms_in_expansion(expr->right)) % MOD;
        }
        else if (expr->otype == ADD){
            return (terms_in_expansion(expr->left) + terms_in_expansion(expr->right)) % MOD;
        }
    }
    return 1;
}
