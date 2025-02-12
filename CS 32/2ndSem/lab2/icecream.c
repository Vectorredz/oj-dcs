#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

enum WeekDay{
    SUNDAY = 0, MONDAY = 1, TUESDAY = 2, WEDNESDAY = 3, THURSDAY = 4, FRIDAY = 5, SATURDAY = 6
};

typedef struct IceCreamStall{ 
    long long int vanilla; // 0
    long long int chocolate; // 1
    long long int strawberry; // 2
    long long int mango; // 3
    long long int oreo; // 4
    long long int matcha; // 5
    long long int pistachio; // 6
    long long int chili; // 7
    double cashier; // 8
} IceCreamStall;


IceCreamStall *newIceCreamStall(){
    // initialize the scoops to 20
    IceCreamStall *p = (IceCreamStall*)malloc(sizeof(IceCreamStall));
    p->chili = 20;
    p->chocolate = 20;
    p->mango = 20;
    p->matcha = 20;
    p->oreo = 20;
    p->pistachio = 20;
    p->strawberry = 20;
    p->vanilla = 20;
    p->cashier = 0;

    return p;
}

int flavorChecker(IceCreamStall *p, char *flavor, enum WeekDay myDay){
    char flavors[8][MAX] = {"vanilla", "chocolate", "strawberry", "mango", "oreo", "matcha", "pistachio", "chili"};
    if (strcmp(flavor, "vanilla") == 0){
        if (p->vanilla > 0){
            if (strcmp(flavors[myDay], "vanilla") == 0){
                p->vanilla -= 1;
            }
            else {
                p->vanilla -= 1;
            }
            return 1;
        }
    }
    if (strcmp(flavor, "chocolate") == 0){
        if (p->chocolate > 0){
            if (strcmp(flavors[myDay], "chocolate") == 0){
                p->chocolate -= 1;
            }
            else {
                p->chocolate -= 1;
            }
            return 1;
        }
    }
    if (strcmp(flavor, "strawberry") == 0){
       if (p->strawberry  > 0){
            if (strcmp(flavors[myDay], "strawberry") == 0){
                p->strawberry -= 1;
            }
            else {
                p->strawberry -= 1;
            }
            return 1;
       }
    }
    return 0;
}

void discountChecker(IceCreamStall *p, char *flavor1, char *flavor2, enum WeekDay myDay, long long int *discounted){
    char flavors[8][MAX] = {"vanilla", "chocolate", "strawberry", "mango", "oreo", "matcha", "pistachio", "chili"};
    if (strcmp(flavor1, "vanilla") == 0 || strcmp(flavor2, "vanilla") == 0 ){
        if (p->vanilla > 0){
            if (strcmp(flavors[myDay], "vanilla") == 0){
                *discounted += 1;
            }
        }
    }
    if (strcmp(flavor1, "chocolate") == 0 || strcmp(flavor2, "chocolate") == 0 ){
        if (p->chocolate > 0){
            if (strcmp(flavors[myDay], "chocolate") == 0){
                *discounted += 1;
            }
        }
    }
    if (strcmp(flavor1, "strawberry") == 0 || strcmp(flavor2, "strawberry") == 0 ){
        if (p->strawberry > 0){
            if (strcmp(flavors[myDay], "strawberry") == 0){
                *discounted += 1;
            }
        }
    }
}


void getOrder(IceCreamStall *p, long long int n, enum WeekDay myDay){
    // brute force
    char lines[n][MAX];
    char flavor1[n][MAX];
    char flavor2[n][MAX];

    long long int discounted = 0; 

    long long int i = 0;

    while (i < n){
        fgets(lines[i], sizeof(lines[i]), stdin);
        i++;
    }

    for (long long int j = 0; j < n; j++){
        long long int num = sscanf(lines[j], "%s %s", flavor1[j], flavor2[j]);  

        // check first if long double input
        if (num == 2){
            int ret1 = flavorChecker(p, flavor1[j], myDay);
            discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
            int ret2 = flavorChecker(p, flavor2[j], myDay);
            if (ret1 && ret2){
                p->cashier += 44.5;
            }
        }
        else {
            int ret1 = flavorChecker(p, flavor1[j], myDay);
            discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
            if (ret1){
                p->cashier += 25.25;
            }
        }
    }
    p->cashier -= (discounted * 5.25);

  
}

enum WeekDay strConverter(char day[]){

    if (strcmp(day, "Monday") == 0){
        return MONDAY;
    }
    if (strcmp(day, "Tuesday") == 0){
        return TUESDAY;
    }
    if (strcmp(day, "Wednesday") == 0){
        return WEDNESDAY;
    }
    if (strcmp(day, "Thursday") == 0){
        return THURSDAY;
    }
    if (strcmp(day, "Friday") == 0){
        return FRIDAY;
    }
    if (strcmp(day, "Saturday") == 0){
        return SATURDAY;
    }
    if (strcmp(day, "Sunday") == 0){
        return SUNDAY;
    }
}

long long int main(){
    // ask for n inputs
    long long int n;
    char day[MAX];
    scanf("%lld %s", &n, day);
    getchar();

    enum WeekDay myDay = strConverter(day);
    IceCreamStall *p = newIceCreamStall();

    getOrder(p, n, myDay);

    printf("%.2lf", p->cashier);

    printf("\n%lld %lld %lld %lld %lld %lld %lld %lld", p->vanilla, p->chocolate, p->strawberry, p->mango, p->oreo, p->matcha, p->pistachio, p->chili);
}