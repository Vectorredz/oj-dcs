#include <stdio.h>
#include <stdlib.h>

int* getSubarray(int arr[], int start, int length) {
    // Allocate memory for the subarray
    int* subarray = (int*)malloc(length * sizeof(int));
    if (subarray == NULL) {
        printf("Memory allocation failed!\n");
        return NULL; // Return NULL if memory allocation fails
    }

    // Copy elements from the original array to the subarray
    for (int i = 0; i < length; i++) {
        subarray[i] = arr[start + i];
    }
    
    return subarray; // Return the subarray
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int start = 1; // Starting index for subarray
    int length = 3; // Length of subarray

    int* subarray = getSubarray(arr, start, length);
    if (subarray != NULL) {
        // Print the subarray
        for (int i = 0; i < length; i++) {
            printf("%d ", subarray[i]);
        }
        printf("\n");

        // Free allocated memory
        free(subarray);
    }

    return 0;
}
