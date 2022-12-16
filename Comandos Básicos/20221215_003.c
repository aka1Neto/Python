#include <stdio.h>

int main(){
    float m, cm;
    printf("Digite o valor em metros: \n");
    scanf("%f", &m);
    cm = m * 100;
    printf("O valor em centimetros eh: %.2f\n", cm);
    return 0;
}