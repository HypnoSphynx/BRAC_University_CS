#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

int main(){
    char str[100];
    char palindrome[100];

    printf("Enter a string: ");
    scanf("%[^\n]s", str);

    int i, j, len;
    len = strlen(str);

    i, j=0;

    for(i=len-1; i>=0; i--){
        palindrome[j]=str[i];
        j++;
    }

    palindrome[j]='\0';

    if(strcmp(str, palindrome)==0){
        printf("Palindrome \n");
    }
    else{
        printf("Not a palindrome \n");
    }


}