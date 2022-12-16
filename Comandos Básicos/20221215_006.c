#include <stdio.h>

int main(){
    float valor_hora, salario;
    int horas_trabalhadas;
    printf("Digite o valor da hora: \n");
    scanf("%f", &valor_hora);
    printf("Digite o numero de horas trabalhadas: \n");
    scanf("%d", &horas_trabalhadas);
    salario = valor_hora * horas_trabalhadas;
    printf("O valor do salario eh: %.2f\n", salario);
    return 0;
}