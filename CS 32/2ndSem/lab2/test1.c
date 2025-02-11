#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 40000

char *strdup(const char *str) {
    char *dup = malloc(strlen(str) + 1);
    if (dup != NULL) {
        strcpy(dup, str);
    }
    return dup;
}



int main(){
    size_t testcases;
    size_t input = 0;
    char buffer[MAX_LENGTH]; // acts as the string for that specific line
    scanf("%d", &testcases);

    char *lines[testcases]; // strings per line

    while (input <= testcases){
        if (fgets(buffer, MAX_LENGTH, stdin)){
            lines[input] = strdup(buffer);
        }
        input++;
    }

    for (int i = 0; i < input; i++){
        printf("%s", lines[i]);
    }
}