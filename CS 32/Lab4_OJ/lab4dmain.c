#include <stdlib.h>
#include "inversions.h"
int64 merge(int64 *s, int left, int mid, int right) {
    int i, j, k; int n1 = mid - left + 1; int n2 = right - mid; int64 inversions = 0; int leftArr[n1], rightArr[n2];
    for (i = 0; i < n1; i++){
        leftArr[i] = s[left + i];
    }
    for (j = 0; j < n2; j++){
        rightArr[j] = s[mid + 1 + j];
    }
    i = 0;
    j = 0;
    k = left;
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            s[k] = leftArr[i];
            i++;
        }
        else {
            s[k] = rightArr[j];
            j++;
            inversions += (n1-i);
        }
        k++;
    }
    while (i < n1) {
        s[k] = leftArr[i];
        i++;
        k++;
    }
    while (j < n2) {
        s[k] = rightArr[j];
        j++;
        k++;
    }
    return inversions;
}
int64 mergeSort(int64 *s, int left, int right) {
    int64 inversions = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        inversions += mergeSort(s, left, mid);
        inversions += mergeSort(s, mid + 1, right);
        inversions += merge(s, left, mid, right);
    }
    return inversions;
}
int64 inversions(int n, int64 *s){
    return mergeSort(s, 0, n-1);
}