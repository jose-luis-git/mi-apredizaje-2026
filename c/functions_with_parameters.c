#include<stdio.h>

int sumar(int*,int*);
int restar(int*,int*);
double dividir(int*,int*);
int multiplicar(int*,int*);

int main(){
    int n1,n2;
    int suma,resta,multiplicacion;
    double division;

    printf("Digite un numero: ");
    scanf("%d", &n1);
    printf("Digite otro numero: ");
    scanf("%d", &n2);

    suma = sumar(&n1, &n2);
    resta = restar(&n1, &n2);
    division = (double)dividir(&n1, &n2);
    multiplicacion = multiplicar(&n1, &n2);

    printf("\nLa suma es: %d\n", suma);
    printf("La resta es: %d\n", resta);
    if(division == -1){
        printf("Error al dividir\n");
    }else{
        printf("La division es: %.2f\n", division);
    }
    printf("La multiplicacion es: %d\n", multiplicacion);

    return 0;
}

int sumar(int*a, int*b){
    return (*a + *b);
}
int restar(int*a, int*b){
    return (*a - *b);
}
double dividir(int*a, int*b){
    if(*b == 0){
        return -1;
    }else{
        return (double)(*a / *b);
    }
}
int multiplicar(int*a, int*b){
    return (*a * *b);
}
