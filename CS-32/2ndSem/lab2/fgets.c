#include <stdio.h>
#include <stdlib.h>
#define MAX 100


int main(){
    int n; // number of orders
    scanf("%d", &n);
    getchar();

    char buffer[n][MAX];
    int i = 0; // number of inputs

    while (i < n){
        fgets(buffer[i], sizeof(buffer[i]), stdin);
        i++;
    }
}
