#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
int t_id[5]={1,2,3,4,5};
void *t_func(int *id);
int main(){
    pthread_t t[5];

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&t[i],NULL,(void *)t_func,&t_id[i]);
        pthread_join(t[i],NULL);
        printf("Thread-%d closed\n",t_id[i]);

    }

    return 0;
}
void *t_func(int *id){
    printf("Thread-%d running\n",*id);
    
}