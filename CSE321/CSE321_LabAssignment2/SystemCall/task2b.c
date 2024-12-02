#include<stdlib.h>
#include<stdio.h>
#include<sys/types.h>



void main(){


    pid_t pid;
    pid =fork();
    if (pid<0){
        printf("Fork failed\n");}
    else if (pid==0){
        pid = fork();
        wait(NULL);
        if (pid<0){
            printf("Fork failed\n");}
        else if (pid==0){
            printf("I am grandchild\n");
        }
        else{
            printf("I am child\n");
        }
    } else {
        wait(NULL);
        printf("I am parent\n");
    }

}


