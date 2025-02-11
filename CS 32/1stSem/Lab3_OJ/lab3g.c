#include <stdio.h>
#include <stdlib.h>

long long int excitingness(int n, long long int *l) {
    long long int sum = 0;
    long long int valley = 0;
    long long int peak = 0;

    for (int i = 0; i < n; i++) {
        if (i > 0 && i < n - 1) {
            if (l[i] < l[i - 1] && l[i] < l[i + 1]) {
                valley++;
            } else if (l[i] > l[i - 1] && l[i] > l[i + 1]) {
                peak++;
            }
        }
        sum += l[i];
    }

    return (valley + peak == 0) ? sum : sum * (valley + peak);
}

long long int* getSubarray(long long int arr[], int start, int length) {
    long long int* subarray = (long long int*)malloc(length * sizeof(long long int));
    if (subarray == NULL) {
        return NULL;
    }
    for (int i = 0; i < length; i++) {
        subarray[i] = arr[start + i];
    }

    return subarray; 
}

long long int excitingness_sum(int n, long long int *l) {
    long long int total_sum = 0;

    for (int start = 0; start < n; start++) {
        for (int length = 1; start + length <= n; length++) {
            long long int *subarray = getSubarray(l, start, length);
            if (subarray != NULL) {
                long long int exc = excitingness(length, subarray);
                total_sum += exc;
                free(subarray);
            }
        }
    }

    return total_sum;
}

int main() {
    long long int arr[] = {1, 3, 4, 4, 4, 2, 6, 1, 2, 5, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    long long int total_excitingness = excitingness_sum(n, arr);
    printf("Total excitingness: %lld\n", total_excitingness);

    return 0;
}
