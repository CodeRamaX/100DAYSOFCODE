#include <stdio.h>
int main(){
    int num,pow;
    double result=1;
    printf("Enter the Number:");
    scanf("%d",&num);
    printf("Enter the power: ");
    scanf("%d",&pow);
    while(pow!=0){
       result*=num;
        pow--;
    }
    printf("Answer is : %.0f",result);
}


