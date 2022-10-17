#include<stdio.h>

int main(){
    int number, index;
    printf("Enter a number");
    scanf("%d", &number);
    index = 2;
    while (index <= number - 1)
    {
        if(number%index==0)
        {
            printf("Not a prime number");
            break;
        }
        index++;
    }
    if(index==number)
        printf("prime number");
}