#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int array[argc-1];

    for (int i = 1; i < argc; i++){
        array[i-1] = atoi(argv[i]);
    }
    for (int i=0 ; i<(argc-1); i++){
        for (int j = i+1; j<(argc-1); j++){
            if (array[i] < array[j]){
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    printf("Descending sorted order is:\n");
    for (int i = 0; i < (argc-1); i++){
        printf("%d ", array[i]);}
    printf("\n");
    return 0;

}