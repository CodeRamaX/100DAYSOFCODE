#include <stdio.h>

int main() {
    int a = 18, b = 20, max;

    // Arithmetic Operators
    printf("Addition: %d\n", a + b);
    printf("Multiplication: %d\n", a * b);

    // Relational Operators
    printf("Is a < b? %d\n", a < b);
    printf("Is a == b? %d\n", a == b);

    // Logical Operators
    printf("(a < b) && (b > 15): %d\n", (a < b) && (b > 15));
    printf("(a > b) || (b > 15): %d\n", (a > b) || (b > 15));

    // Ternary Operator
    max = (a > b) ? a : b;
    printf("Max of a and b: %d\n", max);

    return 0;
}
