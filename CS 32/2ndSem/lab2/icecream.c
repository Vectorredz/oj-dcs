#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 40000

enum WeekDay{
    SUNDAY = 0, MONDAY = 1, TUESDAY = 2, WEDNESDAY = 3, THURSDAY = 4, FRIDAY = 5, SATURDAY = 6
};

typedef struct IceCreamStall{ 
    int vanilla; // 0
    int chocolate; // 1
    int strawberry; // 2
    int mango; // 3
    int oreo; // 4
    int matcha; // 5
    int pistachio; // 6
    int chili; // 7
    double cashier; // 8
} IceCreamStall;


IceCreamStall *newIceCreamStall(){
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
    if (strcmp(flavor, "mango") == 0){
        if (p->mango > 0){
            if (strcmp(flavors[myDay], "mango") == 0){
                p->mango -= 1;
            }
            else {
                p->mango -= 1;
            }
            return 1;
        }
    }
    if (strcmp(flavor, "oreo") == 0){
        if (p->oreo > 0){
            if (strcmp(flavors[myDay], "oreo") == 0){
                p->oreo -= 1;
            }
            else {
                p->oreo -= 1;
            }
            return 1;
        }
    }
    if (strcmp(flavor, "pistachio") == 0){
       if (p->pistachio  > 0){
            if (strcmp(flavors[myDay], "pistachio") == 0){
                p->pistachio -= 1;
            }
            else {
                p->pistachio -= 1;
            }
            return 1;
       }
    }
    if (strcmp(flavor, "chili") == 0){
        if (p->chili  > 0){
            if (strcmp(flavors[myDay], "chili") == 0){
                p->chili -= 1;
            }
            else {
                p->chili -= 1;
            }
            return 1;
        }
     }
}

void discountChecker(IceCreamStall *p, char *flavor1, char *flavor2, enum WeekDay myDay, int *discounted){
    char flavors[8][MAX] = {"vanilla", "chocolate", "strawberry", "mango", "oreo", "matcha", "pistachio", "chili"};
    if (strcmp(flavor1, flavors[myDay]) == 0 || strcmp(flavor2, flavors[myDay]) == 0) {
        *discounted += 1;
    }
}


void getOrder(IceCreamStall *p, int n, enum WeekDay myDay){
    // brute force
    char lines[n][MAX];
    char flavor1[n][MAX];
    char flavor2[n][MAX];

    int discounted = 0; 

    int i = 0;

    while (i < n){
        fgets(lines[i], sizeof(lines[i]), stdin);
        lines[i][strcspn(lines[i], "\n")] = 0;
        i++;
    }

    for (int j = 0; j < n; j++){
        int num = sscanf(lines[j], "%s %s", flavor1[j], flavor2[j]);  

        // check first if long double input
        if (num == 2){
            int flavor1_available = flavorChecker(p, flavor1[j], myDay);
            int flavor2_available = flavorChecker(p, flavor2[j], myDay);

            if (flavor1_available && flavor2_available){
                p->cashier += 44.5;
                discountChecker(p, flavor1[j], flavor1[j], myDay, &discounted);
            }
        }
        else {
            int flavor1_available = flavorChecker(p, flavor1[j], myDay);
            if (flavor1_available){
                p->cashier += 25.25;
                discountChecker(p, flavor1[j], flavor1[j], myDay, &discounted);
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

int main(){
    // ask for n inputs
    int n;
    char day[MAX];
    scanf("%d %s", &n, day);
    getchar();

    enum WeekDay myDay = strConverter(day);
    IceCreamStall *p = newIceCreamStall();

    getOrder(p, n, myDay);

    printf("%.2lf", p->cashier);

    printf("\n%d %d %d %d %d %d %d %d", p->vanilla, p->chocolate, p->strawberry, p->mango, p->oreo, p->matcha, p->pistachio, p->chili);
}