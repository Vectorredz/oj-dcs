#include <stdio.h>

int main(){
    int r = 3;
    int c = 3;

    for (int i = 0; i < r; i++){
        for (int j = 0; j < c-1; j++){
            printf("#");
        }
        printf("#\n");
    }
}