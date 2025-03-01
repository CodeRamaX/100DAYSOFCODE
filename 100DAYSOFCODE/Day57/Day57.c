#include <stdio.h>
#include <math.h>
int count(int num) {
    if (num == 0) {
        return 0;
    }
    return 1 + count(num / 10);
}
int armstrongSum(int num, int power) {
    if (num == 0) {
        return 0;
    }
    int digit = num % 10;
    return pow(digit, power) + armstrongSum(num / 10, power);
}
int main() {
    int num, num_digits, sum;
    printf("Enter a number: ");
    scanf("%d", &num);

    num_digits = count(num); 
    sum = armstrongSum(num, num_digits);  

    if (sum == num) {
        printf("%d is an Armstrong number.\n", num);
    } else {
        printf("%d is not an Armstrong number.\n", num);
    }

    return 0;
}








