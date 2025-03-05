#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define MAX 10000

int my_strlen(char *str) {
    int length = 0;
    int i = 0;
    while (str[i] != '\0'){
        if (str[i] != '\n' &&  str[i] != '\t' && str[i] != ' '){
            length++;
        }
        i++;
    }
    return length;
}

int my_rawlen(char *str){
    int length = 0;
    int i = 0;
    while (str[i] != '\0'){
        length++;
        i++;
    }
    return length;
}

void strip(char *str){
    int i = 0, k = 0;
    int len = my_rawlen(str);
    char stripped[MAX];
    while (i < len){
        if (str[i] != ' '){
            stripped[k++] = str[i];
        }
        i++;
    }
    stripped[k] = '\0'; 

    for (int j = 0; stripped[j] != '\0'; j++){
        str[j] = stripped[j];
    }
    str[k] = '\0';
}

void lowercase(char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(str[i]);
    }
}

char *strdupe(char *str, int strlen){
    char *dupe = malloc((strlen + 1) * sizeof(char));
    if (dupe == NULL) {
        return NULL;
    }
    for (int i = 0; i < strlen; i++){
        dupe[i] = str[i];
    }
    dupe[strlen] = '\0';
    return dupe;
}

void my_strconcat(char *user, char *pass, char *concat, int userlen, int passlen){
    int j = 0;
    for (int i = 0; i < userlen + passlen; i++){
        if (i < userlen){
            concat[i] = user[i];
        }
        else {
            concat[i] = pass[j++];
        }
    }
    concat[userlen + passlen] = '\0';
}

void LPS_array(char *pattern, int patlen, int *lps) {
    int len = 0;
    lps[0] = 0;
    int i = 1;
    while (i < patlen) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len == 0) {
                lps[i] = 0;
                i++;
            } else {
                len = lps[len - 1];
            }
        }
    }
}

int *KMP_search_lower(char *text, int textlen, char *pattern, int patlen, int *numMatches) {
    char *textLower = strdupe(text, textlen);
    char *patternLower = strdupe(pattern, patlen);
    lowercase(textLower);
    lowercase(patternLower);

    int *lps = malloc(patlen * sizeof(int));
    LPS_array(patternLower, patlen, lps);

    int i = 0, j = 0;
    int *positions = malloc(textlen * sizeof(int));
    *numMatches = 0;

    while (i < textlen) {
        if (textLower[i] == patternLower[j]) {
            i++;
            j++;
        }
        if (j == patlen) {
            positions[*numMatches] = i - j;
            (*numMatches)++;
            j = lps[j - 1];
        } else if (i < textlen && textLower[i] != patternLower[j]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    free(textLower);
    free(patternLower);
    free(lps);

    if (*numMatches == 0) {
        positions[0] = -1;
        *numMatches = 1;
    }
    return positions;
}

int exact_match(char *text, char *pattern, int start, int len) {
    for (int i = 0; i < len; i++) {
        if (text[start + i] != pattern[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int n;
    char username[MAX];
    char password[MAX];

    scanf("%s", username);
    scanf("%s", password);
    scanf("%d", &n);
    getchar();

    char buffer[n][MAX];
    for (int i = 0; i < n; i++) {
        fgets(buffer[i], MAX, stdin);
    }

    int userlen = my_strlen(username);
    int passlen = my_strlen(password);
    int found = 0;

    for (int i = 0; i < n; i++) {
        strip(buffer[i]);
        int bufferlen = my_strlen(buffer[i]);
        
        int numUserMatches;
        int *userPositions = KMP_search_lower(buffer[i], bufferlen, username, userlen, &numUserMatches);
        
        if (userPositions[0] != -1) {
            for (int j = 0; j < numUserMatches; j++) {
                int userPos = userPositions[j];
                if (userPos + userlen + passlen <= bufferlen) {
                    if (exact_match(buffer[i], password, userPos + userlen, passlen)) {
                        printf("%d %d\n", i + 1, userPos + 1);
                        found = 1;
                    }
                }
            }
        }
        free(userPositions);
    }

    if (!found) {
        printf("Not leaked!");
    }

    return 0;
}