#include <stdio.h>
int main() {
    float marks[4], total = 0, per;
    char grade;
    int i;
    printf("Enter marks for 4 subjects :\n");
    for (i = 0; i < 4; i++) {
        printf("Subject %d: ", i + 1);
        scanf("%f", &marks[i]);
        total += marks[i];
    }
    per = total / 4;
    int div = (per >= 90) ? 1 :(per >= 80) ? 2 :
    (per >= 70) ? 3:(per >= 60) ? 4 :(per >= 50) ? 5 : 6;
    switch (div) {
        case 1: grade = 'A'; break;
        case 2: grade = 'B'; break;
        case 3: grade = 'C'; break;
        case 4: grade = 'D'; break;
        case 5: grade = 'E'; break;
        default: grade = 'F'; 
    }
    printf("----Results:----\n");
    printf("Total Marks: %.2f/400\n", total);
    printf("Percentage: %.2f%%\n", per);
    printf("Your Grade: %c\n", grade);
    
    if (grade == 'F')
        printf("Failed\n");
    else
        printf("Well done!\n");

    return 0;
}





