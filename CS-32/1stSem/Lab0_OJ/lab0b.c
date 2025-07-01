#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define MAX_LENGTH 400000

char *my_strdup(const char *str) {
    char *dup = malloc(strlen(str) + 1);
    if (dup != NULL) {
        strcpy(dup, str);
    }
    return dup;
}


void strip(char *str){
    int count = 0;
    for (int i = 0; str[i]; i++){
        if (str[i] != ' ')
            str[count++] = str[i];
    }
    str[count] = '\0';
}


void lowercase(char *str, int len){
    for (int i = 0; i < len; i++){
        str[i] = tolower(str[i]);
    }
}

int palindrome(char *str, int len){
    int i = 0;
    int j = len-2;
    int counter = 0;

    while (i < j){
        if (str[i] != str[j]){
            counter++;
        }
        i++;
        j--;
    }
    return counter;
}

int main(){
    int count = 0;
    unsigned int n;
    char buffer[MAX_LENGTH];

    scanf("%u", &n);
    getchar();

    char *lines[n];

    while (count < n){
          if (fgets(buffer, MAX_LENGTH, stdin) != NULL) {
            lines[count] = my_strdup(buffer);
            count++;
        }
    }
    for (int i = 0; i < n; i++){
        strip(lines[i]);
    }

    for (int i = 0; i < n; i++){
        int len = strlen(lines[i]);
        lowercase(lines[i], len);
        int ret = palindrome(lines[i], len);
        free(lines[i]);
        printf("%d\n", ret);
    }
}