#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/msg.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


#define LOGIN_TYPE 1
#define OTP_GENERATOR_TYPE 2
#define MAIL_TYPE 3


struct Message {
    long int type;
    char txt[6];
};



void generateOtp(int msgid);
void verifyMailOtp(int msgid, char otp[]);


int main() {
    int msgid;
    struct Message msg;
    struct Message msg_otp, msg_mail;
    key_t key = 101;

    msgid = msgget((key_t)key, 0666 | IPC_CREAT);
    if (msgid < 0) {
        perror("msgget");
        exit(0);
    }


    char workspace[10];
    printf("Please enter the workspace name: ");
    fgets(workspace, sizeof(workspace), stdin);
    if (strcmp(workspace, "cse321\n") != 0) {
        printf("Invalid workspace name\n");
        exit(0);
    }
    workspace[strcspn(workspace, "\n")] = '\0';  


    msg.type = LOGIN_TYPE;
    strcpy(msg.txt, workspace);

    if (msgsnd(msgid, &msg, sizeof(msg.txt), 0) < 0) {
        perror("msgsnd");
        exit(0);
    }
    printf("Workspace name sent to OTP generator from log in: %s\n", msg.txt);



    pid_t pid_otp = fork();
    if (pid_otp < 0) {
        perror("fork");
        exit(0);
    } else if (pid_otp == 0) {

        generateOtp(msgid);
    } else {

        wait(NULL);


        if (msgrcv(msgid, &msg_otp, sizeof(msg_otp.txt), OTP_GENERATOR_TYPE, 0) < 0) {
        perror("msgrcv");
        exit(0);}
        printf("Log in received OTP from OTP generator: %s\n", msg_otp.txt);


        if (msgrcv(msgid, &msg_mail, sizeof(msg_mail.txt), MAIL_TYPE, 0) < 0) {
            perror("msgrcv");
            exit(0);
        }
        printf("Log in received OTP from mail: %s\n", msg_mail.txt);


        if (strcmp(msg_otp.txt, msg_mail.txt) == 0) {
            printf("OTP Verified\n");
        } else {
            printf("OTP Incorrect\n");
        }


        msgctl(msgid, IPC_RMID, NULL);
    }

    return 0;
}



void generateOtp(int msgid) {
    struct Message msg;


    if (msgrcv(msgid, &msg, sizeof(msg.txt), LOGIN_TYPE, 0) < 0) {
        perror("msgrcv");
        exit(0);
    }
    printf("OTP generator received workspace name from log in: %s\n", msg.txt);

    pid_t otp_pid = getpid();
    snprintf(msg.txt, sizeof(msg.txt), "%d", otp_pid);
    msg.type = OTP_GENERATOR_TYPE;
    if (msgsnd(msgid, &msg, sizeof(msg.txt), 0) < 0) {
        perror("msgsnd");
        exit(0);
    }
    printf("OTP sent to log in from OTP generator: %s\n", msg.txt);


    pid_t pid2=fork();

    if (pid2 < 0) {
        perror("fork");
        exit(0);
    } else if (pid2 == 0) {
        printf("OTP sent to mail from OTP generator: %s\n", msg.txt);
        verifyMailOtp(msgid, msg.txt);
    } else {
        wait(NULL);
    }

    exit(0);
}


void verifyMailOtp(int msgid, char otp[]) {
    struct Message msg;
    printf("Mail received OTP from OTP generator: %s\n", otp);
    strcpy(msg.txt, otp);
    msg.type = MAIL_TYPE;
    if (msgsnd(msgid, &msg, sizeof(msg.txt), 0) < 0) {
        perror("msgsnd");
        exit(0);
    }
    printf("OTP sent to log in from mail: %s\n", msg.txt);
    exit(0);
}
