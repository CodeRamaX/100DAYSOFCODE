#include <stdio.h>
int main(){
    char c;
    printf("Enter the letter to check :");
    scanf("%c",&c);
    switch(c){
    case 'A':case 'E': 
    case 'I':case 'O': 
    case'U':case 'a': 
    case 'e': case 'i': 
    case 'o': case 'u':
    printf("It is an vowel\n");
    break;
    default:
    if((c>='a'&& c<='z') || (c>='A'&& c<='Z'))
    {
        printf("It is a Consonant\n");
    }
    else
    {
        printf("Invalid letter");
    }
    }
    return 0;
}











