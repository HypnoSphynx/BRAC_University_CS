#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<sys/shm.h>
#include<string.h>
#include<sys/ipc.h>
#include<stdbool.h>



struct shared{
    char sel[100];
    int b;
};

void main(){
    int shmid;
    pid_t pid;
    key_t key = 1234;
    struct shared *sh;
    shmid = shmget(key, sizeof(struct shared), IPC_CREAT | 0666);
    sh = shmat(shmid, NULL, 0);
    int pipe[2];




printf("Provide Your Input From Given Options:\n Type a to Add Money\n Type w to Withdraw Money\n Type c to Check Balance\n");
fgets(sh[0].sel, sizeof(sh[0].sel), stdin);
printf("Your selection: %s", sh[0].sel);
sh[0].b = 1000;
pid = fork();

if (pid < 0){
    perror("Fork Failed");
    exit(1);
}

else if (pid==0){
    if (strcmp(sh[0].sel, "a\n")==0){
        printf("Enter the amount to be added: ");
        int am;
        scanf("%d", &am);
        if (am <= 0){
            printf("Adding Failed, Invalid amount\n");
            
        } else{
            sh[0].b =sh[0].b+ am;
            printf("Balance added successfully\n");
            printf("Updated balance after addition:\n%d\n", sh[0].b);
    }

    } else if (strcmp(sh[0].sel, "w\n")==0){
        printf("Enter the amount to be withdrawn: ");
        int am;
        scanf("%d", &am);
        if (am <= 0 || am > sh[0].b){
            printf("Withdraw Failed, Invalid amount\n");
            
        } else{
            sh[0].b =sh[0].b - am;
            printf("Balance withdrawn successfully\n");
            printf("Updated balance after withdrawal:\n%d\n", sh[0].b);
    }
    
    } else if (strcmp(sh[0].sel, "c\n")==0){
        printf("Your current balance is:\n%d\n", sh[0].b);
    } 
    else{
        printf("Invalid Input\n");
        exit(0);}
    
    const char *msg="Thank you for using";
    write(pipe[1], msg, strlen(msg)+1);
    close(pipe[1]);
    exit(0);


}
else{
    wait(NULL);
    char buffer[100];
    int n = read(pipe[0], buffer, 100);
    if (n > 0){
        buffer[n] = '\0';
    } 
    shmdt(sh);
    shmctl(shmid, IPC_RMID, NULL);
    exit(0);
}
}

