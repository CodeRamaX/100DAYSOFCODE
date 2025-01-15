#include <stdio.h>

int main() {
    int id, age;
    float fee;
    char name[50], grade;
    // Input student data
    printf("Enter Student ID: ");
    scanf("%d", &id);
    printf("Enter Student Name: ");
    scanf(" %[^\n]", name); // Reads a string with spaces
    printf("Enter Student Age: ");
    scanf("%d", &age);
    printf("Enter Fee Paid: ");
    scanf("%f", &fee);
    printf("Enter Grade (A/B/C/D/F): ");
    scanf(" %c", &grade);
    // Display student data
    printf("\n--- Student Details ---\n");
    printf("ID: %d\n", id);
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    printf("Fee Paid: %.2f\n", fee);
    printf("Grade: %c\n", grade);

    return 0;
}
