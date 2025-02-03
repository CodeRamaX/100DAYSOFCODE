#include <stdio.h>
int main(){
    char name[100];
    float hours,rate,gross,tax=0,netsalary;
    printf("Enter Employee Name:");scanf("%[^\n]",&name);
    printf("Enter Hours Worked:");scanf("%f",&hours);
    printf("Enter Hourly Rate: ");scanf("%f",&rate);
    gross=hours*rate;
    if(gross>=50000){
        tax=0.20*gross;
    }
    else if(gross>=30000){
        tax=0.15*gross;
    }
    else if (gross>=20000){
        tax=0.10*gross;
    }
    netsalary=gross-tax;

    printf("Payroll Summary for %s:\n", name);
    printf("Gross Salary: %.2f\n", gross);
    printf("Tax Deducted: %.2f\n", tax);
    printf("Net Salary: %.2f\n", netsalary);
}












