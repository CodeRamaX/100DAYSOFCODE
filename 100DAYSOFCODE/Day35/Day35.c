#include <stdio.h>
int main() {
    char ch, choice;
    do {
        printf("Enter a letter: ");
        scanf(" %c", &ch); // Space before %c to handle newline character

        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || 
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            printf("%c is a vowel\n", ch);
        } else {
            printf("%c is a consonant\n", ch);
        }

        printf("Do you want to check another letter? (y/n): ");
        scanf(" %c", &choice); // Space before %c to handle newline character

    } while (choice == 'y' || choice == 'Y');

    printf("Exiting the program. Goodbye!\n");
    return 0;
}






