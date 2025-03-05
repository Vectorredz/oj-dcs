#include <stdio.h>

// Function to compute the LPS (Longest Prefix Suffix) array
void computeLPSArray(char *pat, int M, int *lps) {
    int len = 0;  // Length of previous longest prefix suffix
    int i = 1;
    lps[0] = 0;   // LPS of first char is always 0

    while (i < M) {
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// KMP search function
int KMPSearch(char *text, char *pattern) {
    int N = 0, M = 0;  // Get lengths of text and pattern

    // Calculate lengths manually (since we can't use `strlen`)
    while (text[N] != '\0') N++;
    while (pattern[M] != '\0') M++;

    int lps[M];  // LPS array
    computeLPSArray(pattern, M, lps);

    int i = 0, j = 0;  // i -> text index, j -> pattern index
    while (i < N) {
        if (text[i] == pattern[j]) {
            i++;
            j++;
        }
        if (j == M) {
            return i - j;  // Found pattern at index (i - j)
        } else if (i < N && text[i] != pattern[j]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return -1;  // Not found
}

// Main function to test the algorithm
int main() {
    char string1[] = "test";
    char string2[] = "dwadawdtestdwadaw";

    int index = KMPSearch(string2, string1);
    if (index != -1)
        printf("String found at index %d\n", index);
    else
        printf("String not found\n");

    return 0;
}
