#include <stdio.h>
#include <stdlib.h>

typedef struct deque{
    int *array;
    int size;
    int left;
    int right;
} Deque;

Deque *init(int n){
    Deque *d = malloc(sizeof(Deque));
    d->size = n;
    d->array = malloc(sizeof(int) * d->size);
    d->left = (int)(d->size / 2) + 1;
    d->right = (int)(d->size / 2);
    return d;
}

void enqueue_left(Deque *d, int x){
    d->array[d->left--] = x; 
}

void enqueue_right(Deque *d, int x){
    d->array[d->right++] = x; 
}

void dequeue_right(Deque *d){
    d->array[d->right--]; 
}

void dequeue_left(Deque *d){
    d->array[d->left++]; 
}

int deque_empty(Deque *d){ 
    if (d->left > d->right){
        return 1;
    }
    return 0;
}

int deque_full(Deque *d){
    if (d->right == d->size || d->left == 0){
        return 1;
    }
    return 0;
}


int main(){
    int n = 5;
    Deque *d = init(n);
    enqueue_right(d,1);

    printf("%d", d->array[--d->right]);

    // for (int i = d->left + 1; i <= d->right; i++){
    //     printf("%d %d\n", i, d->array[i]);
    // }
    
}