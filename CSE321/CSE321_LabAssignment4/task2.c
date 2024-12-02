#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define MaxCrops 5 
#define warehouseSize 5 
#define MaxIterations 5 

sem_t empty;
sem_t full;
int in = 0;
int out = 0;
char crops[warehouseSize] = {'R', 'W', 'P', 'S', 'M'}; 
char warehouse[warehouseSize] = {'N', 'N', 'N', 'N', 'N'}; 
pthread_mutex_t mutex;

void *Farmer(void *farmer_id) {
    int id = *((int *)farmer_id);
    for (int i = 0; i < MaxIterations; i++) {
        sem_wait(&empty);
        pthread_mutex_lock(&mutex);
        char crop = crops[in]; 
        warehouse[in] = crop;
        printf("Farmer %d: Inserts crop %c at %d\n", id, crop, in);
        in = (in + 1) % warehouseSize;
        sleep(1);

        pthread_mutex_unlock(&mutex);
        sem_post(&full);
    }

    printf("Farmer %d: %s\n", id, warehouse);
    pthread_exit(NULL);
}

void *ShopOwner(void *owner_id) {
    int id = *((int *)owner_id);
    for (int i = 0; i < MaxIterations; i++) {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);
        char crop = warehouse[out];
        warehouse[out] = 'N';
        printf("Shop owner %d: Removes crop %c from %d\n", id, crop, out);
        out = (out + 1) % warehouseSize;
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);
    }

    printf("Shop owner %d: %s\n", id, warehouse);
    pthread_exit(NULL);
}

int main() {
    pthread_t farmer_threads[5], shop_owner_threads[5];
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty, 0, warehouseSize); 
    sem_init(&full, 0, 0); 

    int farmer[5] = {1, 2, 3, 4, 5};
    int shop_owner[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++) {
        pthread_create(&farmer_threads[i], NULL, Farmer, &farmer[i]);
        pthread_create(&shop_owner_threads[i], NULL, ShopOwner, &shop_owner[i]);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(farmer_threads[i], NULL);
        pthread_join(shop_owner_threads[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}