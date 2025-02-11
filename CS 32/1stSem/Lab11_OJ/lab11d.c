#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sensousness.h"

#define MAXLENGTH 5 * (10 * 10 * 10)

int64_t dp[MAXLENGTH + 1][MAXLENGTH + 1];

int64_t min(int64_t x, int64_t y);
int64_t senSAUCEness(const char *str, int first, int last);
int64_t sensuousness_sum(const char *s);
void init_memo (int n);


int64_t min(int64_t x, int64_t y){
    if (x < y){
        return x;
    }
    else {
        return y;
    }
}

int64_t senSAUCEness(const char *str, int first, int last){
    // base case 

    if (first > last){
        return 0;
    }
    if (first == last){
        return 0;
    }

    // if seen in memo / dp 
    if (dp[first][last] != -1 ){
        return dp[first][last];
    }

    if (str[first] == str[last]){
        dp[first][last] = senSAUCEness(str, first + 1, last);

    }

    int64_t del_first_char = 1 + senSAUCEness(str, first + 1, last);
    int64_t del_last_char = 1 + senSAUCEness(str, first, last - 1);

    dp[first][last] = min(del_first_char, del_last_char);
    return dp[first][last];
}


int64_t sensuousness_sum(const char *s) {
    int64_t senSauce_tot = 0;
    
    int lenStr = strlen(s);
    // initially set memo / dp 
    init_memo(lenStr);
    
     for (int first = 0; first < lenStr; first++) {
        for (int last = first; last < lenStr; last++) {
            senSauce_tot += senSAUCEness(s, first, last);
        }
    }

    return senSauce_tot;
    
}

void init_memo (int n){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = -1;
        }
    }
}

int main(){
    int64_t ret = sensuousness_sum("philip");
    printf("%lu ", ret);

    int64_t ret1 = sensuousness_sum("z");
    printf("%lu ", ret1);

    int64_t ret2 = sensuousness_sum("zZ");
    printf("%lu ", ret2);

}