#include<stdio.h>
#include<sys/types.h>

countProcess=0;

void main(){
    pid_t a,b,c;

    a=fork(); 
    b=fork(); 
    c=fork(); 

    if (a==0){ 
        countProcess++; //xounting parent process
        printf("Child %d process ID: %d\n",countProcess, getpid());
        if (getpid()%2 !=0){
            countProcess++; //counting if only the child process is created
            fork();
             
        }
    }
    else if (b==0){ 
        countProcess++;
        printf("Child %d process ID: %d\n",countProcess, getpid());
        if (getpid()%2 !=0){
            countProcess++; //counting if only the child process is createds
            fork();
            
        }
    }

    else if (c==0){ 
        countProcess++;
        printf("Child %d process ID: %d\n",countProcess, getpid());
        if (getpid()%2 !=0){
            countProcess++; //counting if only the child process is created
            fork();
        }
    }
    printf("Total number of processes created: %d\n", countProcess);

 

    

}
