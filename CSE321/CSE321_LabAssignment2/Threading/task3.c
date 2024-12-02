#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>

void *calculateSum(void *args);

int main() {
    pthread_t t[3];
    char username[3][20];
    int sum[3];
    for (int i = 0; i < 3; i++) {
        printf("Username %d: ", i + 1);
        scanf("%s", username[i]);
        pthread_create(&t[i], NULL, calculateSum, (void *)username[i]);
    }

    for (int i = 0; i < 3; i++) {
        pthread_join(t[i], (void **)&sum[i]);
    }

    printf("Sum of ASCII values of the names: %d %d %d\n", sum[0], sum[1], sum[2]);
    if (sum[0] == sum[1] && sum[1] == sum[2]) {
        printf("Youreka");
    } else if (sum[0] == sum[1] || sum[1] == sum[2] || sum[0] == sum[2]) {
        printf("Miracle");
    } else {
        printf("Hasta la vista");
    }

    return 0;
}
void *calculateSum(void *args) {
    char *name = (char *)args;
    int sum =0;
    int i=0;
    while (i<strlen(name)) {
        sum += *name++;
    }
    pthread_exit((void *)sum);
}

