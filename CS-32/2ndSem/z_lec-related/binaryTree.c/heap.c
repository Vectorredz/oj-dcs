#include <stdio.h>
#include <stdlib.h>
#define MAX 1000

typedef struct heap{
    int array[MAX];
    int size;
} Heap;

int parent(int i) { return (i-1)/2; }
int left(int i) { return 2*i + 1; }
int right(int i) { return 2*i + 2; }

int main(){

}