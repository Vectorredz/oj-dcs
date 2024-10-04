#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tabulate.h"

// void tabulate(int r, int c, char **headers, long long int **data) {
    
//     int lens[c];
//     int j = 0;
//     for (int i = 0; i < c; i++) {
//         lens[j++] = strlen(headers[i])+1;
//         if (i == c-1){
//             printf("| %*s |", lens[i], headers[i]);
//         }
//         else {
//             printf("| %*s ", lens[i], headers[i]);
//         }
//     }
//     printf("\n");

//     for (int i = 0; i < r; i++) {
//         for (int j = 0; j < c; j++) {
//             if (j == c-1){
//                 printf("| %*lld |", lens[j], data[i][j]);
//             }
//             else {
//                 printf("| %*lld ", lens[j], data[i][j]);

//             }
//         }
//         printf("\n");
//     }
// }

int main() {
    int *headers[] = {{1,2}, {2,3}};

    for (int i = 0; i < 2; i++){
        printf("%d ", headers[i]);
    }

    char *cheaders[] = {"abc", "def", "ghi"};

     for (int i = 0; i < 3; i++){
        printf("%s ", cheaders[i]);
    }

}
