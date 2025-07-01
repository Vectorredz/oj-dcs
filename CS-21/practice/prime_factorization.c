
#include <stdio.h>
#include <stdlib.h>

int is_prime(int num){
    
    if (num <= 1) return 0;
    if (num == 2 || num == 3) return 1;
    if (num % 2 == 0) return 0;
    if (num % 3 == 0) return 0;
    for (int i = 5; i * i <= num; i++){
        if (num % i == 0 || num % (i + 2) == 0){
            return 0;
        }
    }
    return 1;

}

void prime_factorization(int num){

    for (int i = 2; i <= num; i++){
        while (num % i == 0 && is_prime(i)){
            num = num / i;
            printf("%d ", i);
        }
    }
    return;
}



int main(){
    int a;

    scanf("%d", &a);
    prime_factorization(a);
}











