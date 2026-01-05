#include<stdio.h>

void exchange(int*,int*);

int main(){
    int number1, number2;

    printf("Enter a number: ");
    scanf("%d", &number1);
    printf("Enter another number: ");
    scanf("%d", &number2);


    //swap the values of number1 and number2

    printf("\n--Before swap--\n");
    printf("original number1: %d\n", number1);
    printf("original number2: %d\n", number2);

    exchange(&number1, &number2);
    printf("\n--Value swap--\n");
    printf("After swap number1: %d\n", number1);
    printf("After swap number2: %d\n", number2);

    return 0;
}
void exchange(int*number1, int*number2){
    int aux = *number1;
    *number1 = *number2;
    *number2 = aux;
}
