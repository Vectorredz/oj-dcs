#include <stdio.h>
#define MOD 1000000000

unsigned long int excitement(unsigned int s1, unsigned int s2, unsigned long int total){
    unsigned long int ret = 0;
    if (total % 2 == 0){
        ret += total + s1 + s2 + 1;
        ret %= MOD;
    }
    else{
        ret += total;
        ret %= MOD;
    }
    return ret;
}

unsigned long int combinatorics(unsigned long int *skills, unsigned long int n){
    unsigned long int final = 0;
    unsigned long int ret = 1;
    unsigned int z = 0;
    for (unsigned int u = 0; u < n; u++){
        for (unsigned int v = u; v < n; v++){
            if (u != v) {
                ret = skills[u] * skills[v];
                final += excitement(skills[u], skills[v], ret);
                final %= MOD;
                z++;
            }
        }
    }
    return final;
}

int main(){
    unsigned int t;
    unsigned long int n;
    unsigned long int skills[100000000];
    unsigned long int prod[300000];
    unsigned int count = 0;
    
    scanf("%u", &t);
    for (unsigned int i = 0; i < t; i++){
        scanf("%lu", &n);
        for (unsigned int j = 0; j < n; j++){
            scanf("%lu", &skills[j]);
        } 
        prod[count] = combinatorics(skills, n);
        count++;
    }
    for (unsigned int p = 0; p < count; p++){
        printf("%lu\n", prod[p]);
    }
}