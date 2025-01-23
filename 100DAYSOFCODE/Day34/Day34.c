#include <stdio.h>

int main() {
    int a, b, c;
    char *tri_type;

    printf("Enter the three sides of the triangle: ");
    scanf("%d %d %d", &a, &b, &c);
    tri_type = (a + b > c && a + c > b && b + c > a) ? 
                    (a == b && b == c) ? "Equilateral Triangle" : 
                    (a == b || b == c || a == c) ? "Isosceles Triangle" : 
                    "Scalene Triangle" : 
                    "Not a Triangle";

    printf("The triangle is: %s\n", tri_type);

    return 0;
}


