#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    int array[argc - 1];
    int i;
    for (i = 1; i < argc; i++) {
        array[i - 1] = atoi(argv[i]);
    }
    int n = argc - 1;
    pid_t pid = fork();
    if (pid == 0) {
        char *args[] = {"./sort", argv[1], argv[2], argv[3], argv[4], argv[5],argv[6],argv[7],argv[8],argv[9],argv[10], NULL}; //exe files are in the same directory
        execvp(args[0], args);
    } else {
        wait(NULL);
        printf("Odd/Even status:\n");
        char *args[] = {"./oddeven", argv[1], argv[2], argv[3], argv[4], argv[5],argv[6],argv[7],argv[8],argv[9],argv[10], NULL}; //exe files are in the same directory
        execvp(args[0], args);
    }
    return 0;
}