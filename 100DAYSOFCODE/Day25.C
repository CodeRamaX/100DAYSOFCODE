#include <stdio.h>

int main() {
    char name[50];
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You are %d years old.\n", age);
    printf("What is your name? ");
    scanf("%s", name);

    printf("Hello, %s! Welcome to learning C.\n", name);

    return 0;
}
#include <stdio.h>


