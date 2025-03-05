#include <stdio.h>
#include <stdlib.h>

void kadanes(float *arr, int n) {
    int l = 0, r = 0;  // Initialize left and right pointers
    float res = arr[0]; // Initialize the result with the first element
    float maxEnding = arr[0]; // Initialize the maximum ending here
    int temp_l = 0; // Temporary left pointer to track the start of the current subarray

    for (int i = 1; i < n; i++) {
        // Update the maximum ending here
        if (maxEnding + arr[i] > arr[i]) {
            maxEnding = maxEnding + arr[i];
        } else {
            maxEnding = arr[i];
            l = i; // Reset the temporary left pointer
        }

        // Update the result and the right pointer if we found a better subarray
        if (maxEnding > res) {
            res = maxEnding;
            r = i;       // Update the right pointer
        }
    }

    // Print the left and right indices of the maximum subarray
    printf("%d %d\n", l, r);
}

int main() {
    int n;
    scanf("%d", &n);
    float arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%f", &arr[i]);
    }

    kadanes(arr, n);

    return 0;
}