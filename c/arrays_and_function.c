#include<stdio.h>

void maximum(int*, int);
void minimum(int*, int);
void average(int*, int);

int main(){
    //maximun size of the array
    int size;
    while(1){
        printf("Enter the array size: ");
        scanf("%d", &size);
        if((size >= 1) && (size <= 10)){
            break;
        }else{
            printf("\nEnter the size again\n");
            continue;
        }
    }

    int array[size];

    for(int i=0;i<size;i++){
        printf("Enter a number: ");
        scanf("%d", array + i);
    }

    maximum(array, size);
    minimum(array, size);
    average(array, size);

    return 0;
}
void maximum(int*array, int size){
    int max = array[0];
    for(int i=1;i<size;i++){
        if(*(array + i) > max){
            max = *(array + i);
        }
    }
    printf("\nThe maximun number in the array is: %d\n", max);
}
void minimum(int*array, int size){
    int min = array[0];
    for(int i=1;i<size;i++){
        if(*(array + i) < min){
            min = *(array + i);
        }
    }
    printf("The minimum number in the array is: %d\n", min);
}
void average(int*array, int size){
    int sum = 0;
    double Average;

    for(int i=0;i<size;i++){
        sum += *(array + i);
    }
    Average = (double)sum / size;
    printf("The average of the numbers is: %.2f\n", Average);
}
