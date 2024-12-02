#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){

char a[100],b[100];

printf("Enter sentence: ");
scanf("%[^\n]s", a);

int i,j,len;
len=strlen(a);
j=0;

for (i=0; i<len; i++){
    if (a[i] != ' '){
        b[j]=a[i];
        j++;
    }
    else if (a[i]==' ' && a[i+1]!=' '){
        b[j]=a[i];
        j++;
    }
    else{
        continue;
    }


}

b[j]='\0';

printf("%s \n", b);

}