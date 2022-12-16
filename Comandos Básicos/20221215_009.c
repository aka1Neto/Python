#include <stdio.h>

int main(){
    int n1, n3;
    float n2, resultado;
    printf("Digite os 3 numeros: \n");
    scanf("%d%f%d", &n1, &n2, &n3);
    resultado = (2 * n1) * (n2 / 2);
    printf("O produto do dobro do primeiro com metade do segundo: %2.f\n", resultado);
    resultado = (3 * n1) + n3;
    printf("A soma do triplo do primeiro com o terceiro: %.2f\n" ,resultado);
    resultado = n3 * n3 *n3;
    printf("O terceiro elevado ao cubo eh: %.2f\n", resultado);
    return 0;
}