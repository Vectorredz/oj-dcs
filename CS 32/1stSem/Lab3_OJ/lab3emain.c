// excitingness = sum (niceness) * no. of peaks and valleys
// peak - x3 < xi > x2; valley - x3 > xi < x2 

#include <stdio.h>
#include <stdlib.h>
#include "excitingness.h"

long long int excitingness(int n, long long int *l)
{
    long long int sum = 0;
    long long int valley = 0;
    long long int peak = 0;
    if (n == 0) return 0;
    for (int i = 0; i < n; i++)
    {
        if (i > 0 && i < n-1)
        {
            if (l[i] < l[i-1] && l[i] < l[i+1])
            {
                valley++;
            }
            else if (l[i] > l[i-1] && l[i] > l[i+1])
            {
                peak++;
            }
        }
        sum += l[i];
    }
    if (valley + peak == 0)
    {
        return sum;
    }
    return sum * (valley + peak);
}
int main()
{
    long long int list[] = {2};
    long long int len = sizeof(list) / sizeof(list[0]);
    long long int ret = excitingness(len, list);
    printf("%d ", ret);


}