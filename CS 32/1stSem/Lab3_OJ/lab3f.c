#include <stdlib.h>
#include "excitingnesses.h"

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
    return sum * (valley + peak);
}
long long int *excitingnesses(int n, long long int *l)
{
    long long int *res = (long long int*)malloc(n * sizeof(long long int));
    for (int i = 0; i < n; i++)
    {
        long long int *sub = (long long int*)malloc((n-1) * sizeof(long long int));
        for (int j = 0, k = 0; j < n; j++)
        {
            if (i != j)
            {
                sub[k++] = l[j];
            }
        }
        res[i] = excitingness(n-1, sub);
    }
    return res;
}