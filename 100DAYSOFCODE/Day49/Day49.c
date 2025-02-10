#include <stdio.h>
int main() {
    int num, original, reversed = 0, digit;
    printf("Enter a number: ");
    scanf("%d", &num);
    original = num;  
    while (num != 0) {
        digit = num % 10;  
        reversed = reversed * 10 + digit;  
        num /= 10;  
    }
    printf("Reversed number: %d\n", reversed);
    
    if (original == reversed) {
        printf("The number is a palindrome!\n");
    } else {
        printf("The number is not a palindrome.\n");
    }
    return 0;
}










