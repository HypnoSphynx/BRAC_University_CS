#include<stdio.h>
#include<stdlib.h>

struct Paratha{

    int quantity;
    int price;
};

struct Vegetables{

    int quantity;
    int price;
};

struct MineralWater{
    
        int quantity;
        int price;
};

int main(){

    int numPeople;
    int split;
    struct Paratha paratha;
    struct Vegetables vegetables;
    struct MineralWater mineralwater;

    printf("Quantity of Paratha: ");
    scanf("%d",&paratha.quantity);
    printf("Unit Price: ");
    scanf("%d",&paratha.price);
    printf("Quantity of Vegetables: ");
    scanf("%d",&vegetables.quantity);
    printf("Unit Price: ");
    scanf("%d",&vegetables.price);
    printf("Quantity of Mineral Water: ");
    scanf("%d",&mineralwater.quantity);
    printf("Unit Price: ");
    scanf("%d",&mineralwater.price);
    printf("Number of people: ");
    scanf("%d",&numPeople);

    int totalCost = paratha.quantity*paratha.price + vegetables.quantity*vegetables.price + mineralwater.quantity*mineralwater.price;
    split=totalCost/numPeople;
    

    printf("Individiual people will pay: %d\n",split);

    return 0;
}

