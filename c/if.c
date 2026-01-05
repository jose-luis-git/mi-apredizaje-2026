#include<stdio.h>

int main(){
    int n1,n2;
    int suma=0,resta=0,multiplicacion=0;
    double division=0;

    printf("Digite un numero: ");
    scanf("%d", &n1);
    printf("Digite otro numero: ");
    scanf("%d", &n2);

    suma = n1 + n2;
    resta = n1 - n2;
    multiplicacion = n1 * n2;

    printf("\nLa suma es: %d\n", suma);
    printf("La resta es: %d\n", resta);
    if(n2 == 0){
        printf("Error al dividir\n");
    }else{
        division = (double)n1 / n2;
        printf("La division es: %.2f\n", division);
    }
    printf("La multiplicacion es: %d\n", multiplicacion);

    return 0;
}
