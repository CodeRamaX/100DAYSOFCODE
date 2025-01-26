#include <stdio.h>
int main() {
    int n,n1=0,n2=1,c;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");
    
    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            printf("%d ", n1);
            continue;
        }
        if (i == 2) {
            printf("%d ", n2);
            continue;
        }
        c = n1 + n2;
        n1 = n2;
        n2 = c;

        printf("%d ", c);
    }

    return 0;
}

















