#include <stdio.h>
#include <stdlib.h>

int main(){
    int n = 5;
    int m = 5;
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < n; j++){
            printf("*");
        }
        printf("\n");
        n -= 1;
    }
}