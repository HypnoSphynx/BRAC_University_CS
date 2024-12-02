#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
int t_id[5]={0,1,2,3,4};
void *t_func(int *id);
int count=1;
int main(){
    pthread_t t[5];

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&t[i],NULL,(void *)t_func,&t_id[i]);
        pthread_join(t[i],NULL);

    }
    return 0;
}
void *t_func(int *id){

    for (int j=0; j<5;j++){
        printf("Thread %d prints %d\n",*id,count);
        count++;}
    
}