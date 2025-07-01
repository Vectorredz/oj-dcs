#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

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
    // initialize the scoops to 20
    IceCreamStall *p = (IceCreamStall*)malloc(sizeof(IceCreamStall));
    p->chili = 20;
    p->chocolate = 2;
    p->mango = 20;
    p->matcha = 20;
    p->oreo = 20;
    p->pistachio = 20;
    p->strawberry = 20;
    p->vanilla = 20;
    p->cashier = 0;

    return p;
}

int oneScoopChecker(IceCreamStall *p, char *flavor, enum WeekDay myDay, int order){
    char flavors[8][MAX] = {"vanilla", "chocolate", "strawberry", "mango", "oreo", "matcha", "pistachio", "chili"};
    if (strcmp(flavor, "vanilla") == 0){
        if (p->vanilla > 0){
            p->vanilla -= 1;
            return 1;
        }
    }
    if (strcmp(flavor, "chocolate") == 0){
        if (p->chocolate > 0){
            p->chocolate -= 1;
            return 1;
        }
    }
    if (strcmp(flavor, "strawberry") == 0){
        if (p->strawberry > 0){
            p->strawberry -= 1;
            return 1;
        }
    }

    return 0;
}



int doubleScoopChecker(IceCreamStall *p, char *flavor1, char *flavor2, enum WeekDay myDay, int order){
    char flavors[8][MAX] = {"vanilla", "chocolate", "strawberry", "mango", "oreo", "matcha", "pistachio", "chili"};

    // same order 
    
    if (strcmp(flavor1, "vanilla") == 0 && strcmp(flavor2, "vanilla") == 0){
        // check if they are valid
        if (p->vanilla > 1){
            p->vanilla -= 2; 
            return 1;
        } // means there are enough for double scoop
        return 0;
    }
    if (strcmp(flavor1, "chocolate") == 0 && strcmp(flavor2, "chocolate") == 0){
        // check if they are valid
        if (p->chocolate > 1){
            p->chocolate -= 2; 
            return 1;
        } // means there are enough for double scoop
        return 0;
    }
    if (strcmp(flavor1, "strawberry") == 0 && strcmp(flavor2, "strawberry") == 0){
        // check if they are valid
        if (p->strawberry > 1){
            p->strawberry -= 2; 
            return 1;
        } // means there are enough for double scoop
        return 0;
    }

    if (strcmp(flavor1, "vanilla") == 0 && strcmp(flavor2, "chocolate") == 0){
        // check if they are valid
        if (p->vanilla >= 1 && p->chocolate >= 1){
            p->vanilla -= 1; 
            p->chocolate -=1;
            return 1;
        } // means there are enough for double scoop
        return 0;
    }

    if (strcmp(flavor1, "chocolate") == 0 && strcmp(flavor2, "vanilla") == 0){
        // check if they are valid
        if (p->vanilla >= 1 && p->chocolate >= 1){
            p->vanilla -= 1; 
            p->chocolate -=1;
            return 1;
        } // means there are enough for double scoop
        return 0;
    }

    if (strcmp(flavor1, "vanilla") == 0 && strcmp(flavor2, "strawberry") == 0){
        // check if they are valid
        if (p->vanilla >= 1 && p->strawberry >= 1){
            p->vanilla -= 1; 
            p->strawberry -=1;
            return 1;
        } // means there are enough for double scoop
        return 0;
    }

    if (strcmp(flavor1, "strawberry") == 0 && strcmp(flavor2, "vanilla") == 0){
        // check if they are valid
        if (p->vanilla >= 1 && p->strawberry >= 1){
            p->vanilla -= 1; 
            p->strawberry -=1;
            return 1;
        } // means there are enough for double scoop
        return 0;
    }

    if (strcmp(flavor1, "chocolate") == 0 && strcmp(flavor2, "strawberry") == 0){
        // check if they are valid
        if (p->chocolate >= 1 && p->strawberry >= 1){
            p->chocolate -= 1; 
            p->strawberry -=1;
            return 1;
        } // means there are enough for double scoop
        return 0;
    }

     if (strcmp(flavor1, "strawberry") == 0 && strcmp(flavor2, "chocolate") == 0){
        // check if they are valid
        if (p->chocolate >= 1 && p->strawberry >= 1){
            p->chocolate -= 1; 
            p->strawberry -=1;
            return 1;
        } // means there are enough for double scoop
        return 0;
    }


    // call one scoopy checker for different approaches
    int ret1 = oneScoopChecker(p, flavor1, myDay, 1); // first order
    int ret2 = oneScoopChecker(p, flavor2, myDay, 1); // second order
    if (ret1 && ret2) return 1;
    return 0;
}

void discountChecker(IceCreamStall *p, char *flavor1, char *flavor2, enum WeekDay myDay, int *discounted){
    char flavors[8][MAX] = {"vanilla", "chocolate", "strawberry", "mango", "oreo", "matcha", "pistachio", "chili"};
    if (strcmp(flavor1, "vanilla") == 0 || strcmp(flavor2, "vanilla") == 0 ){
        if (strcmp(flavors[myDay], "vanilla") == 0){
            *discounted += 1;
        }
    }
    if (strcmp(flavor1, "chocolate") == 0 || strcmp(flavor2, "chocolate") == 0 ){
        if (strcmp(flavors[myDay], "chocolate") == 0){
            *discounted += 1;
        }
    }
    if (strcmp(flavor1, "strawberry") == 0 || strcmp(flavor2, "strawberry") == 0 ){
        if (strcmp(flavors[myDay], "strawberry") == 0){
            *discounted += 1;
        }
    }

    // other flavors

}

int is_validFlavor(char *flavor){
    return (strcmp(flavor, "vanilla") == 0 || strcmp(flavor, "chocolate") == 0 || strcmp(flavor, "strawberry") == 0 || strcmp(flavor, "mango") == 0 || strcmp(flavor, "oreo") == 0 || strcmp(flavor, "matcha") == 0 || strcmp(flavor, "pistachio") == 0 || strcmp(flavor, "chili") == 0) ? 1 : 0;
}

int is_validInput(int scoop, char *flavor1, char *flavor2){
    int flag1 = 0; // flag for first flavor
    int flag2 = 0; // flag for second flavor
    if (scoop == 2){ // check each input
        // check first input if valid
        flag1 = is_validFlavor(flavor1);
        flag2 =  is_validFlavor(flavor2);

        if (flag1 && flag2) return 1; // valid double scoup
        else return 0;
    }
    else if (scoop == 1){
        flag1 = is_validFlavor(flavor1);
        flag2 =  is_validFlavor(flavor2);

        if (flag1 || flag2) return 1; // single scoop
        else return 0; // invalid input
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
        i++;
    }

    for (int j = 0; j < n; j++){
        int scoop = sscanf(lines[j], "%s %s", flavor1[j], flavor2[j]);  
        // printf("-> \n%d ", p->vanilla);
        if (scoop == 2){
            if (is_validInput(scoop, flavor1[j], flavor2[j])){ // valid double scoop
                int ret = doubleScoopChecker(p, flavor1[j], flavor2[j], myDay, scoop);
                if (ret){
                    discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
                    p->cashier += 44.50;
                }
            }
            else if (!is_validInput(scoop, flavor1[j], flavor2[j]) && ((is_validFlavor(flavor1[j])) && !(is_validFlavor(flavor2[j])))  ){ // the first order is valid but the second is not
                int ret = oneScoopChecker(p, flavor1[j], myDay, scoop);
                if (ret){
                    discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
                    p->cashier += 25.25;
                }
            }
            else if (!is_validInput(scoop, flavor1[j], flavor2[j]) && (!(is_validFlavor(flavor1[j])) && (is_validFlavor(flavor2[j])))){ // the first order is valid but the second is not
                int ret = oneScoopChecker(p, flavor2[j], myDay, scoop);
                if (ret){
                    discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
                    p->cashier += 25.25;
                }
            }
        }
        else if (scoop == 1){
            if (is_validInput(scoop, flavor1[j], flavor2[j]) && ((is_validFlavor(flavor1[j])) && !(is_validFlavor(flavor2[j])))  ){ // the first order is valid but the second is not
                int ret = oneScoopChecker(p, flavor1[j], myDay, scoop);
                if (ret){
                    discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
                    p->cashier += 25.25;
                }
            }
            else if (is_validInput(scoop, flavor1[j], flavor2[j]) && (!(is_validFlavor(flavor1[j])) && (is_validFlavor(flavor2[j])))){ // the first order is valid but the second is not
                int ret = oneScoopChecker(p, flavor2[j], myDay, scoop);
                if (ret){
                    discountChecker(p, flavor1[j], flavor2[j], myDay, &discounted);
                    p->cashier += 25.25;
                }
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

    free(p);
}