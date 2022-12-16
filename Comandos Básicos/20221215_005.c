#include <stdio.h>

int main(){
    float lado, area;
    printf("Digite o lado do quadrado: \n");
    scanf("%f", &lado);
    area = lado * lado;
    printf("A area do quadrado eh: %2.f\n", area);
    printf("O dobro da area do quadrado eh: %2.f\n", area * 2);
    return 0;
}