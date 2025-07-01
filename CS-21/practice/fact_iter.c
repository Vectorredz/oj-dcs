#include <stdio.h>
#include <stdlib.h>

int fact_iter(int n) {
    int ret = 1;
   
    for (int k = 2; k <= n; k++) {
      ret *= k;
    }
   
    return ret;
  }

int main(){
    printf("%d",fact_iter(4));
}