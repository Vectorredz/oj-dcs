#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);

    if (num <= 0){
        return 0;
    } else if (num == 1){
        printf("0");
        return 0;
    } else if (num == 2){
        printf("1");
        return 0;
    }

    int a = 0;
    int b = 1;
    int fibn;

    for (int i = 3; i <= num; i++) {
        fibn = a + b;
        a = b;
        b = fibn;
    }

    printf("%d",fibn);
}