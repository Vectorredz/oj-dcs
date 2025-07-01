#include <stdio.h>
#include <stdlib.h>
#define MAX 50

int main(){

    int test_cases;
    scanf("%d", &test_cases);
    getchar();

    char initial_url[MAX];

    fgets(initial_url, MAX, stdin);

    while (test_cases--){
        int command_count = 0;

        scanf("%d", &command_count);
        getchar();
        for (int i = 0; i < command_count; i++){
            fgets(initial_url, MAX, stdin);
        }
    }
}