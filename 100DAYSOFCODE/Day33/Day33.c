#include <stdio.h>

int main() {
    int num, i, is_prime;
    printf("Enter a number: ");
    scanf("%d", &num);
    is_prime = (num > 1) ? 1 : 0; 
    for (i = 2; i * i <= num; i++) {
        is_prime = (num % i == 0) ? 0 : is_prime;
    }

    printf("%d is %s\n", num, (is_prime ? "a prime number" : "not a prime number"));
    return 0;
}






