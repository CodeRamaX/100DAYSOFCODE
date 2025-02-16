#include <stdio.h>

int main() {
    int start, end;
    printf("Enter start year: ");
    scanf("%d", &start);
    printf("Enter end year: ");
    scanf("%d", &end);

    printf("Leap years between %d and %d:\n", start, end);
    for (int year = start; year <= end; year++) {
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
            printf("%d ", year);
        }
    }
    return 0;
}
















