#include<stdlib.h>
#include<stdio.h>

int checkPerfect(int n);

int main(){
    int from;
    int to;
    printf("Enter the range: ");
	scanf("%d", &from);
	printf("Enter the range to: ");
	scanf("%d", &to);
	
	for (int i=from;i<=to;i++){
		if (i==checkPerfect(i)){
			printf("%d \n", i);
		};
	};
	return 0;
};

int checkPerfect(int number){
	int sum=0;
	for (int i=1;i<number;i++){
		if (number%i==0){
			sum = sum + i;
		};
	};
	if (sum==number){
		return number;
		}
};