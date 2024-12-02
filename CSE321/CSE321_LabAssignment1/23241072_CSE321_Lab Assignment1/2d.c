#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>


int main(){
    char email[100];
    char valid[]= "sheba.xyz";
    char checkValid[15];
    bool atFound=false;

    printf("Enter your email: ");

    scanf("%s", email);

    int i, j, len;
    j=0;
    len = strlen(email);

    for (i=0; i<len; i++){
        if (email[i]=='@'){
            atFound=true;
            i++;
        }
        if (atFound==true){
            checkValid[j]=email[i];
            j++;
        }
    }

    checkValid[j]='\0';

    if (strcmp(checkValid, valid)==0){
        printf("Email address is okay \n");
    }
    else{
        printf("Email address is outdated \n");
    }

}