#include <stdio.h>

int main(){
    char ptr[6] = "CS 21\n";
    char *s0 = ptr;
    // s0 += 0;
    printf("%p %p", s0, s0 + 1);
} 