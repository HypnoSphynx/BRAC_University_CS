#include<stdio.h>
#include<stdlib.h>


int main(){
    int a,b;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("Enter another number: ");
    scanf("%d", &b);


    if(a>b){
        int sum = a-b;
        printf("Subtraction: %d \n", sum);
    }
    else if(a<b){
        int sum = a+b;
        printf("Addition: %d \n", sum);
    }
    else{
        int sum=a*b;
        printf("Multiplication: %d \n", sum);
    }
}
