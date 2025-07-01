#include <stdio.h>
#include <stdlib.h>
#include "imbalances.h"

int64 *imbalances(int n, int64 *s)
{
    int64 curr_sum = 0;
    int64 *prefix_sum = (int64*)malloc(n * sizeof(int64));
    int64 *team2 = (int64*)malloc((n-1) * sizeof(int64));
    int64 *results = (int64*)malloc((n-1) * sizeof(int64));
    for (int i = 0; i < n; i++)
    {
        curr_sum += s[i];
        prefix_sum[i] = curr_sum;
    }

    int64 pivot = 0;
    pivot = prefix_sum[(n-1)];

    for (int i = 0; i < n-1; i++)
    {
        team2[i] = (pivot - prefix_sum[i]); 

        results[i] = (team2[i] - prefix_sum[i]);
        if (results[i] < 0)
        {
            results[i] *= -1;
        }
    }
    return results;
}



int main()
{   
    int64 list[] = {3,1,4,1,5};
    int64 *ret = imbalances(5, list);
    for (int i = 0; i < 4; i++)
    {
        printf("%lld ", ret[i]);
    }
}