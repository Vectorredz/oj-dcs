#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define MAX 40

enum WeekDay {
    SUNDAY = 0, MONDAY = 1, TUESDAY = 2, WEDNESDAY = 3, THURSDAY = 4, FRIDAY = 5, SATURDAY = 6
};

typedef struct IceCreamStall {
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

IceCreamStall *newIceCreamStall() {
    IceCreamStall *p = (IceCreamStall *)malloc(sizeof(IceCreamStall));
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

bool useFlavor(IceCreamStall *p, char *flavor) {
    if (strcmp(flavor, "vanilla") == 0 && p->vanilla > 0) {
        p->vanilla--;
        return true;
    }
    if (strcmp(flavor, "chocolate") == 0 && p->chocolate > 0) {
        p->chocolate--;
        return true;
    }
    if (strcmp(flavor, "strawberry") == 0 && p->strawberry > 0) {
        p->strawberry--;
        return true;
    }
    if (strcmp(flavor, "mango") == 0 && p->mango > 0) {
        p->mango--;
        return true;
    }
    if (strcmp(flavor, "oreo") == 0 && p->oreo > 0) {
        p->oreo--;
        return true;
    }
    if (strcmp(flavor, "matcha") == 0 && p->matcha > 0) {
        p->matcha--;
        return true;
    }
    if (strcmp(flavor, "pistachio") == 0 && p->pistachio > 0) {
        p->pistachio--;
        return true;
    }
    if (strcmp(flavor, "chili") == 0 && p->chili > 0) {
        p->chili--;
        return true;
    }
    return false;
}

void applyDiscount(IceCreamStall *p, char *flavor1, char *flavor2, enum WeekDay myDay, double *discount) {
    char *flavorOfTheDay;
    switch (myDay) {
        case SUNDAY: flavorOfTheDay = "vanilla"; break;
        case MONDAY: flavorOfTheDay = "chocolate"; break;
        case TUESDAY: flavorOfTheDay = "strawberry"; break;
        default: return;
    }

    if (strcmp(flavor1, flavorOfTheDay) == 0 || strcmp(flavor2, flavorOfTheDay) == 0) {
        *discount += 5.25;
    }
}

void getOrder(IceCreamStall *p, int n, enum WeekDay myDay) {
    char lines[n][MAX];
    char flavor1[n][MAX];
    char flavor2[n][MAX];

    double totalDiscount = 0;

    for (int i = 0; i < n; i++) {
        fgets(lines[i], sizeof(lines[i]), stdin);
        lines[i][strcspn(lines[i], "\n")] = 0;
    }

    for (int j = 0; j < n; j++) {
        int num = sscanf(lines[j], "%s %s", flavor1[j], flavor2[j]);

        if (num == 2) {
            bool flavor1Available = useFlavor(p, flavor1[j]);
            bool flavor2Available = useFlavor(p, flavor2[j]);

            if (flavor1Available && flavor2Available) {
                p->cashier += 44.5;
                applyDiscount(p, flavor1[j], flavor2[j], myDay, &totalDiscount);
            }
        } else {
            bool flavorAvailable = useFlavor(p, flavor1[j]);

            if (flavorAvailable) {
                p->cashier += 25.25;
                applyDiscount(p, flavor1[j], flavor1[j], myDay, &totalDiscount);
            }
        }
    }

    p->cashier -= totalDiscount;
}

enum WeekDay strConverter(char day[]) {
    if (strcmp(day, "Monday") == 0) return MONDAY;
    if (strcmp(day, "Tuesday") == 0) return TUESDAY;
    if (strcmp(day, "Wednesday") == 0) return WEDNESDAY;
    if (strcmp(day, "Thursday") == 0) return THURSDAY;
    if (strcmp(day, "Friday") == 0) return FRIDAY;
    if (strcmp(day, "Saturday") == 0) return SATURDAY;
    if (strcmp(day, "Sunday") == 0) return SUNDAY;
    return -1;
}

int main() {
    int n;
    char day[MAX];
    scanf("%d %s", &n, day);
    getchar();

    enum WeekDay myDay = strConverter(day);
    IceCreamStall *p = newIceCreamStall();

    getOrder(p, n, myDay);

    printf("%.2lf\n", p->cashier);
    printf("%d %d %d %d %d %d %d %d\n", p->vanilla, p->chocolate, p->strawberry, p->mango, p->oreo, p->matcha, p->pistachio, p->chili);

    free(p);
    return 0;
}