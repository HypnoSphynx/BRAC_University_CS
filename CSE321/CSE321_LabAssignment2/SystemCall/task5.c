#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
    pid_t parent, child, grandchild1, grandchild2, grandchild3;
    printf("1. Parent process ID %d\n",parent, getpid());

    child=fork();
    //child process
    if(child==0){
        printf("2. Child process ID %d\n", getpid());
        grandchild1=fork();

        //grandchild process 1
        if(grandchild1==0){
            printf("3. Grandchild process ID %d\n", getpid());
            grandchild2=fork();

            //grandchild process 2
            if(grandchild2==0){
                printf("4. Grandchild process ID %d\n", getpid());
                grandchild3=fork();

                //grandchild process 3
                if(grandchild3==0){
                    printf("5. Grandchild process ID %d\n", getpid());
                } 
            }
        }
    }
}
    
