#include <stdio.h>
int main() {
    char op;  
    double num1, num2, result;
    printf("Enter the two numbers and char with space: ");
    scanf("%lf %lf", &num1, &num2);
    scanf(" %c", &op);  
    switch (op) {
        case '+':
            result = num1 + num2;
            printf("Result: %.1f + %.1f = %.1f\n", num1, num2, result);
            break;
        case '-':
            result = num1 - num2;
            printf("Result: %.2f - %.2f = %.2f\n", num1, num2, result);
            break;
        case '*':
            result = num1 * num2;
            printf("Result: %.2f * %.2f = %.2f\n", num1, num2, result);
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                printf("Result: %.2f / %.2f = %.2f\n", num1, num2, result);
            } else {
                printf("Error \n");
            }
            break;
        default:
            printf("Invalid Operator\n");
    }
    return 0;
}





