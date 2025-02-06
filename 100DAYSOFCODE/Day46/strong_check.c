#include <stdio.h>
int main() {
    int num, d, sum = 0, fact, i;
    printf("Enter the number: ");
    scanf("%d", &num);
    int num1 = num;  
    while (num1 != 0) {
        d = num1 % 10;  
        fact = 1;
        for (i = 1; i <= d; i++)  
            fact *= i;

        sum += fact; 
        num1 /= 10;   
    }
    if (sum == num)
        printf("Strong number\n");
    else
        printf("Not a strong number\n");
    return 0;
}

