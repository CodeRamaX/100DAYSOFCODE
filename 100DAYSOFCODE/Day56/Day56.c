#include <stdio.h>
#include <string.h>

int checkAnagram(const char *str1, const char *str2);
void sortString(char *str);

int main() {
    char str1[100], str2[100];

    printf("Enter the first string: ");
    fgets(str1, sizeof(str1), stdin);
    str1[strcspn(str1, "\n")] = '\0';  // Remove newline character

    printf("Enter the second string: ");
    fgets(str2, sizeof(str2), stdin);
    str2[strcspn(str2, "\n")] = '\0';  // Remove newline character

    if (checkAnagram(str1, str2)) {
        printf("\"%s\" and \"%s\" are anagrams.\n", str1, str2);
    } else {
        printf("\"%s\" and \"%s\" are not anagrams.\n", str1, str2);
    }

    return 0;
}

int checkAnagram(const char *str1, const char *str2) {
    if (strlen(str1) != strlen(str2)) {
        return 0;
    }

    char sortedStr1[100], sortedStr2[100];
    strcpy(sortedStr1, str1);
    strcpy(sortedStr2, str2);

    sortString(sortedStr1);
    sortString(sortedStr2);

    return strcmp(sortedStr1, sortedStr2) == 0;
}

void sortString(char *str) {
    int charCount[256] = {0};
    int length = strlen(str);

    for (int i = 0; i < length; i++) {
        charCount[(unsigned char)str[i]]++;
    }

    int index = 0;
    for (int i = 0; i < 256; i++) {
        while (charCount[i] > 0) {
            str[index++] = i;
            charCount[i]--;
        }
    }
    str[index] = '\0';
}
