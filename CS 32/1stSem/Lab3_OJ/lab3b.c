#include <stdlib.h>
#include "squares.h"

int squareroot(int num) {
    if (num < 0) return 0; 
    int left = 0, right = num;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        long long square = (long long)mid * mid;
        if (square == num) return 1; 
        else if (square < num) left = mid + 1;
        else right = mid - 1;
    }
    return 0; 
}

int squares(struct node *head, int **res)
{
    struct node *curr = head;
    int re_sized = 0;
    while (curr){
        if (squareroot(curr->val) || curr->val == 0){
            re_sized++;
        }
        curr = curr->next;
    }
    int *array = (int*)malloc(re_sized * sizeof(int));
    if (!array) return 0;
    int i = 0;
    curr = head;
    while (curr){
        if (squareroot(curr->val) || curr->val == 0){
            array[i++] = curr->val;
        }
        curr = curr->next;
    }
    *res = array;
    return re_sized;
}