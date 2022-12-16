#include <stdio.h>

int main(){
    int a, b, soma;
    printf("Digite os numeros que voce deseja somar: \n");
    scanf("%d%d", &a, &b);
    soma = a + b;
    printf("O resultado da soma eh %d\n", soma);
    return 0;
}