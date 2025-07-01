#include <stdio.h>
#include <stdlib.h>
#include "friends.h"

typedef struct dict {
    int idx;
    int count;
} dict;

dict **sort(int n, int *f);

friends *guess_friends(int n, int *f) {
    friends *res = malloc(sizeof(friends));
    res->pairs = malloc(n * sizeof(friend_pair));  

    // SORT f in decreasing order
    dict **sorted_idx = sort(n, f);

    // CHECK if odd: impossible pairing; even: possible pairing

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += f[i];
    }
    if (sum % 2 != 0) {
        res->count = -1;
        free(res->pairs);
        free(res);
        return res;
    }

    res->count = 0;

    int *remaining_f = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        remaining_f[sorted_idx[i]->idx] = f[sorted_idx[i]->idx];
    }

    for (int i = 0; i < n; i++) {
        if (remaining_f[sorted_idx[i]->idx] == 0) {
            continue; 
        }

        int p1 = sorted_idx[i]->idx;
        for (int j = i + 1; j < n; j++) {
            if (remaining_f[sorted_idx[j]->idx] == 0) {
                continue; 
            }

            int p2 = sorted_idx[j]->idx;
            if (remaining_f[p1] > 0 && remaining_f[p2] > 0) {
                res->pairs[res->count].person1 = p1;
                res->pairs[res->count].person2 = p2;
                res->count++;
                remaining_f[p1]--;
                remaining_f[p2]--;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (remaining_f[i] > 0) {
            res->count = -1;
            free(remaining_f);
            free(res->pairs);
            free(res);
            return res;
        }
    }
    return res;
}


dict **sort(int n, int *f) {

    dict **dictio = malloc(n * sizeof(dict *));
    for (int i = 0; i < n; i++) {
        dict *person = malloc(sizeof(dict));
        person->count = f[i];
        person->idx = i;
        dictio[i] = person;
    }

    dict *temp = malloc(sizeof(dict));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (dictio[j]->count < dictio[j + 1]->count) {
                temp = dictio[j];
                dictio[j] = dictio[j + 1];
                dictio[j + 1] = temp;
            }
        }
    }

    return dictio;
}

int main(){
    int n = 6;
    int f[] = {2,2,0,2,1,3};
    friends *res = guess_friends(n, f);
    for (int i = 0; i < n; i++){
        printf("%d ", res[i].pairs);
    }
}
