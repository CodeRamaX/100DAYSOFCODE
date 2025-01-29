#include <stdio.h>
void greet() {
    printf("This introduction to Functions in C.\n");
}
int add(int a, int b) {
    return a + b;
}
int max(int x, int y) {
    return (x > y) ? x : y;
}
int main() {
    int num1, num2;
    greet();
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);
    printf("Sum: %d\n", add(num1, num2));  
    printf("Max: %d\n", max(num1, num2));
    return 0;
}









