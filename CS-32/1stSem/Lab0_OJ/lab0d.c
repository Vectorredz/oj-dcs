#include <stdio.h>
#include <string.h>

unsigned long int planting(unsigned long int  start, unsigned long int end, unsigned long int *height){
    unsigned long int ret = 0;
    for (unsigned int i = start; i <= end; i++){
        ret += height[i];
    }
    return ret;
}
void water_plants(unsigned long int *height, unsigned int plant){
    for (unsigned int  i = 0; i < plant; i++){
        height[i] += 2;
    }
}

int main(){
    unsigned int test_cases;
    scanf("%d", &test_cases);
    unsigned int plant;
    unsigned long int height[100000];
    unsigned int counter = 0;
    unsigned long int res[300000];
    
    // initialize test cases; plant heights
    for (unsigned int  i = 0; i < test_cases; i++){
        scanf("%u",  &plant);
        for (unsigned int  j = 0; j < plant; j++){
            scanf("%lu", &height[j]);   
        }
        // initialize actions; days
        unsigned long int q;
        scanf("%lu", &q);
        unsigned int  i[q], j[q];
        char action[q];
        unsigned int  k = 0;
        while (k < q){
            scanf("%s", &action);
            if (strcmp(action, "total")==0){
                scanf("%u %u", &i[k], &j[k]);
                res[counter++] = planting(i[k]-1, j[k]-1, height);
            }
            else {
                water_plants(height, plant);
            }
            k++;
    }
    
    }
    for (unsigned int  l = 0; l < counter; l++){
        printf("%lu\n", res[l]);
    }
}