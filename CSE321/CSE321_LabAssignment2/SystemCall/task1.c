#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>
#include<stdbool.h>

int main(int argc, char *argv[]) {
    int file;
    
    file = open(argv[1],O_CREAT | O_WRONLY);
    char buff[100];
    while (true) {
        printf("Enter string: ");
        fgets(buff, 100, stdin);
        if (strcmp(buff, "-1\n") == 0) {
            break;
        }
        write(file, buff, strlen(buff));
    }
    close(file);
    return 0;
}