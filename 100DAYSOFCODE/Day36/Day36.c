
/*-----Write a C program to display the sum of all even numbers and the product 
of all odd numbers within a given range. The user should input the starting and ending numbers of the range. 
Use conditionals to determine even and odd numbers, and a loop to process the range.-----*/

#include <stdio.h>
int main(){
    int num,r1,r2,even_sum=0;
    long long int odd_mul=1;

    printf("Enter the starting number: ");
    scanf("%d",&r1);
    printf("Enter the ending number: ");
    scanf("%d",&r2);
    for (num=r1;num<=r2;num++){
        if (num%2==0){
            even_sum+=num;
        }
        else{
            odd_mul*=num;
        }
    }
    printf("Sum of even numbers:%d\n",even_sum);
    printf("Product of odd numbers:%lld\n",odd_mul);
}








