#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

int main(){
    printf("Enter your password: ");
    char password[100];
    scanf("%s", password);

    int i, len;
    len= strlen(password);

    bool hasDigit = false;
    bool hasUpper = false;
    bool hasLower = false;
    bool hasSpecial = false;
    bool printed=true;

    for(i=0; i<len; i++){
        if(password[i]>='0' && password[i]<='9'){
            hasDigit = true;
        }
        else if(password[i]>='A' && password[i]<='Z'){
            hasUpper = true;
        }
        else if(password[i]>='a' && password[i]<='z'){
            hasLower = true;
        }
        else if (password[i]=='_' || password[i]=='$' || password[i]=='#' || password[i]=='@'){
            hasSpecial = true;
        }
    }



if (hasDigit && hasUpper && hasLower && hasSpecial){
    printf("Ok \n");
}
else{
    if (!hasDigit){
        printf("Digit Missing");
        printed=true;
    }
    if (!hasUpper){
        if (printed){
            printf(", ");
        }
        printf("Uppercase character missing");
        printed=true;
    }
    if (!hasLower){
        if (printed){
            printf(", ");
        }
        printf("Lowercase character missing");
        printed=true;
    }
    if (!hasSpecial){
        if (printed){
            printf(", ");
        }
        printf("Special character missing");
    }

}
}
