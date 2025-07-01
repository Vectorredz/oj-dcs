#include <stdio.h>
#include <stdlib.h>

int find(int x, int *father){
    if (!father[x]){
        return x;
    }
    else{
        find(father[x], father);
    }
}

int main(){
    int *father = malloc(sizeof(int) * 4); 
    for (int i = 0; i < 4; i++) father[i] = i+1;

    int y = find(3, father);
    printf("%d ", y);
}