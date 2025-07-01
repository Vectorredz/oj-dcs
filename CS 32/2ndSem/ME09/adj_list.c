#include <stdio.h>
#include <stdlib.h>

/*

Father : forest represented by single arra

*/

int *INIT_FATHER(int n){
    int *FATHER = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) FATHER[i] = -1;

    return FATHER;
}

void UNION(int *FATHER, int i, int j){
    int count = FATHER[i] + FATHER[j];
    if (abs(FATHER[i]) > abs(FATHER[j])){
        FATHER[j] = i;
        FATHER[i] = count;
    }
    else {
        FATHER[i] = j;
        FATHER[j] = count;
    }
    return;
}

int FIND(int *FATHER,  int i){
    int r = i;
    while (FATHER[r] > 0){
        r = FATHER[r];
    }
    int j = i;
    while (j != r){
        int k = FATHER[j];
        FATHER[j] = r;
        j = k;
    }
    return r;
}

int TEST(int *FATHER, int k, int l){
    k = FIND(FATHER, k);
    l = FIND(FATHER, l);
    if (k == l) return 1;
    else return 0;

}

int main(){
    int n; 
    scanf("%d ", &n);
    
    n = abs(n);
    int i, j;

    int *FATHER = INIT_FATHER(n);
    int counter = 0;
    while (1){
        scanf("%d %d", &i, &j);
        // while (FATHER[i] > 0){
        //     i = FATHER[i];
        // }
        // while (FATHER[j] > 0){
        //     j = FATHER[j];
        // }
        // if (i != j) FATHER[i] = j;
        if (i == 0 && j == 0) break;
        i = FIND(FATHER, i);
        j = FIND(FATHER, j);
        if (i != j){
            UNION(FATHER, i, j);
            counter++;
        }
    }

    printf("%d ", n-counter+1);
    // for (int i = 0; i < 5; i++){
    //     printf("%d ", FATHER[i]);
    // }
}

 
